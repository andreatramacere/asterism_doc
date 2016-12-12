.. _src_detection_process_user_guide:

src_detection process user guide
================================

.. contents:: :local:



.. toctree::

.. currentmodule:: asterism.analysis_processes.source_detection


Introduction
------------
This modules describe   the :class:`~asterism.analysis_processes.source_detection.DoSrcDetectionProcess`
class used to implement the source detection process.


The tasks  in the process are:
 * :class:`~asterism.analysis_tasks.image_processing.image_processing.DoImageProcessing`, Image filtering by convolution
 * :class:`~asterism.analysis_tasks.source_detection.background_estimation.background_estimation.DoSetBkgThreshTask`, estimate of the bkg level and th.
   (:ref:`bkg_estimation_task_user_guide`)
 * :class:`~asterism.analysis_tasks.source_detection.image_segmentation.image_segmentation.DoImageSegmentationTask`, image segmentation (dbscan,NN,seg map)
   (:ref:`image_segmentation_task_user_guide`)
 * :class:`~asterism.analysis_tasks.source_detection.deblending.deblending.DoSetDeblendingMethodTask`, sets the deblending method
 * :class:`~asterism.analysis_tasks.source_detection.deblending.denclue_deblending.DoDENCLUEDeblendingTask`, denclue-based deblending
   (:ref:`denclue_deblending_task_user_guide`)
 * :class:`~asterism.analysis_tasks.source_detection.deblending.gauss_laplace_deblending.DoGLWDeblendingTask`, gauss-laplace watershed based deblending
   (:ref:`glw_deblending_task_user_guide`)
 * :class:`~asterism.analysis_tasks.source_detection.image_segmentation.catalog.DoSourceCatalogTask`, catalog production, and source filtering
 * :class:`~asterism.analysis_tasks.source_detection.deblending.deblending.DoDeblendingValidationTask` validates the deblended products
   and produces the final list of detected source clusters (:ref:`deblending_validation_task_user_guide`)

These tasks  are orchestrated by the :func:`~asterism.analysis_processes.source_detection.do_src_detection_process_func`,
and the corresponding flow chart of the function is shown by the following diagram.

.. figure:: src_detection_process.png
    :width: 100%
    :align: center
    :figclass: align-center

    schematic view of the source detection pipeline flow chart



.. rubric:: Processes API


.. autosummary::
    ~asterism.analysis_processes.source_detection.DoSrcDetectionProcess

.. autosummary::
    ~asterism.analysis_processes.source_detection.do_src_detection_process_func



Tasks userguide
------------------
    * :ref:`bkg_estimation_task_user_guide`
    * :ref:`image_segmentation_task_user_guide`
    * :ref:`denclue_deblending_task_user_guide`
    * :ref:`glw_deblending_task_user_guide`

Processes userguide
-------------------



Command line tutorial
---------------------


Python scripts tutorial
-----------------------



