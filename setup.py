from setuptools import setup, find_packages

setup(
    name="tw.jquery.fancybox",
    version="0.0",
    description="jQuery FancyBox integration for ToscaWidgets",
    author="Nils Philippsen",
    author_email="nils@tiptoe.de",
    #url=
    #download_url=
    install_requires=["ToscaWidgets>=0.9.8", "tw.jquery>=0.9.5"],
    packages=find_packages(),
    namespace_packages = ['tw.jquery'],
    zip_safe=False,
    include_package_data=True,
    #test_suite="nose.collector"
    package_data={"tw.jquery.fancybox": ["static/*"]},
    entry_points="""
        [toscawidgets.widgets]
        widgets = tw.jquery.fancybox
        #samples = tw.jquery.fancybox.samples
        #resource = tw.jquery.fancybox.resources
    """,
    keywords = ["toscawidgets.widgets"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Environment :: Web Environment :: ToscaWidgets",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Widget Sets",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
