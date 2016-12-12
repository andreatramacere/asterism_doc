"""

"""

from asterism import data_dir
from asterism.core.image_manager.image import Image
from asterism.analysis_tasks.source_detection.background_estimation.background_estimation import DoSetBkgThreshTask
import pylab as plt


fig,ax=plt.subplots(1,1)
image=Image.from_fits_file(data_dir+'/galaxy.fits')
ax.imshow(image._data,interpolation='nearest')

bkg_task=DoSetBkgThreshTask()
bkg_task.list_parameters()
bkg_task.set_par('plot',value=True)
bkg_task.set_par('skewness_range',value=0.1)
bkg_task.set_par('sub_block_frac_size',value=0.1)

bkg_threshold,bkg_mode,bkg_sig=bkg_task.run(image=image)



from asterism import data_dir
from asterism.core.image_manager.image import Image
from asterism.analysis_tasks.source_detection.background_estimation.background_estimation import set_thresh
import pylab as plt


fig,ax=plt.subplots(1,1)
image=Image.from_fits_file(data_dir+'/galaxy.fits')
ax.imshow(image._data,interpolation='nearest')

bkg_threshold,bkg_mode,bkg_sig=set_thresh(image,sub_block_frac_size=0.1,skewness_range=0.1,plot=True)

