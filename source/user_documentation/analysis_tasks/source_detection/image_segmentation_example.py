"""

"""

from asterism import data_dir
from asterism.core.image_manager.image import Image
from asterism.analysis_tasks.source_detection.background_estimation.background_estimation import DoSetBkgThreshTask
from asterism.analysis_tasks.source_detection.image_segmentation.image_segmentation import DoImageSegmentationTask
import  numpy as np

image=Image.from_fits_file(data_dir+'/galaxy.fits')

bkg_task=DoSetBkgThreshTask()
bkg_task.list_parameters()
bkg_task.set_par('plot',value=False)
bkg_task.set_par('skewness_range',value=0.1)
bkg_task.set_par('sub_block_frac_size',value=0.1)

bkg_threshold,bkg_mode,bkg_sig=bkg_task.run(image=image)
print bkg_threshold,bkg_mode,bkg_sig
image_seg_task=DoImageSegmentationTask()
image_seg_task.list_parameters()
image_seg_task.set_par('bkg_threshold',value=float(bkg_threshold))
image_seg_task.set_par('K',value=1.5)
image_seg_task.set_par('K_pix',value=True)
image_seg_task.set_par('plot_dbscan',value=True)
image_seg_task.list_parameters()

image_seg_task.run(image=image)


from asterism import data_dir
from asterism.core.image_manager.image import Image
from asterism.analysis_tasks.source_detection.background_estimation.background_estimation import set_thresh
from asterism.analysis_tasks.source_detection.image_segmentation.image_segmentation import do_image_segmentation

image=Image.from_fits_file(data_dir+'/galaxy.fits')
bkg_threshold,bkg_mode,bkg_sig=set_thresh(image,sub_block_frac_size=0.1,skewness_range=0.1,plot=False)
do_image_segmentation(image,bkg_threshold,K=np.float_(1.5),K_pix=True,plot_dbscan=True)
