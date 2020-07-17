# patching statistics for GPU

from PyHEADTAIL.gpu import gpu_wrap
import PyHEADTAIL.general.pmath as pm

from PyHEADTAIL.particles import particles

particles.Particles_backup = particles.Particles

class Particles_thrustSlicing(particles.Particles):
    stat_get_slices = particles.Particles_backup.get_slices
    def get_slices(self, slicer, *args, **kwargs):
        if pm.device == 'GPU':
            stats = kwargs.get('statistics', [])
            if stats is True:
                kwargs['statistics'] = [
                    'mean_x', 'mean_y', 'mean_z',
                    'mean_xp', 'mean_yp', 'mean_dp',
                    'sigma_x', 'sigma_y', 'sigma_z', 'sigma_dp',
                    'epsn_x', 'epsn_y', 'epsn_z',
                    'eff_epsn_x', 'eff_epsn_y'
                ]
                stats = kwargs['statistics']
            do_x = False
            try:
                stats.remove('mean_x')
                do_x = True
            except ValueError:
                pass
            try:
                stats.remove('sigma_x')
                do_x = True
            except ValueError:
                pass
            do_y = False
            try:
                stats.remove('mean_y')
                do_y = True
            except ValueError:
                pass
            try:
                stats.remove('sigma_y')
                do_y = True
            except ValueError:
                pass
            do_z = False
            try:
                stats.remove('mean_z')
                do_z = True
            except ValueError:
                pass
            try:
                stats.remove('sigma_z')
                do_z = True
            except ValueError:
                pass
            do_dp = False
            try:
                stats.remove('mean_dp')
                do_dp = True
            except ValueError:
                pass
            try:
                stats.remove('sigma_dp')
                do_dp = True
            except ValueError:
                pass
            if len(stats) == 0:
                kwargs.pop('statistics', False)
        slices = self.stat_get_slices(slicer, *args, **kwargs)
        if pm.device == 'GPU':
            if do_x:
                mx, sx = gpu_wrap.thrust_mean_and_std_per_slice(slices, self.x)
                slices.mean_x = mx
                slices.sigma_x = sx
            if do_y:
                my, sy = gpu_wrap.thrust_mean_and_std_per_slice(slices, self.y)
                slices.mean_y = my
                slices.sigma_y = sy
            if do_z:
                mz, sz = gpu_wrap.thrust_mean_and_std_per_slice(slices, self.z)
                slices.mean_z = mz
                slices.sigma_z = sz
            if do_dp:
                mdp, sdp = gpu_wrap.thrust_mean_and_std_per_slice(
                    slices, self.dp)
                slices.mean_dp = mdp
                slices.sigma_dp = sdp
        return slices

particles.Particles = Particles_thrustSlicing
