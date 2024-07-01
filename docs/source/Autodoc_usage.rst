Autodoc usage
=====

.. _Here are some ways to use Autodoc:

You can also edit the content in between autodoc features
------------

One class in the ``file`` module of PyCSI is

.. autoclass:: file.File


One function in the ``file`` module of PyCSI is

.. autofunction:: file.File.save

The lock state of the model can be modified through the `.lock` property. This Boolean represents the lock/unlocked state of the model. Set this property to `True` or `False` to modify the lock state of the model.
Use the ``.analysis.run_analysis()`` method to start the analysis of the model.

.. autofunction:: analysis.Analysis.run_analysis


The `.analysis` property gives access to the Analyze menu commands. The following functions are available:
Use ``.analysis.set_load_cases_to_run()`` to set the load cases to Run / Do not run.

.. autofunction:: analysis.Analysis.set_load_cases_to_run
