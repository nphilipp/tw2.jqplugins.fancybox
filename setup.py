from setuptools import setup, find_packages

setup(
    name="tw2.jquery.fancybox",
    version="0.0",
    description="jQuery FancyBox integration for ToscaWidgets 2",
    author="Nils Philippsen",
    author_email="nils@tiptoe.de",
    #url=
    #download_url=
    install_requires=["tw2.core>=2.0", "tw2.jquery>=2.0"],
    packages=find_packages(),
    namespace_packages = ['tw2', 'tw2.jquery'],
    zip_safe=False,
    include_package_data=True,
    #test_suite="nose.collector"
    package_data={"tw2.jquery.fancybox": ["static/*"]},
    entry_points="""
        [tw2.widgets]
        widgets = tw2.jquery.fancybox
    """,
    keywords = ["tw2.widgets"],
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
