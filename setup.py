from setuptools import setup

setup(
    name='KivyMD-AKivymd-Sylvia-Dynamic',
    version='0.1',
    packages=['kivymd_akivymd_sylvia_dynamic', 'kivymd_akivymd_sylvia_dynamic.uix',
              'kivymd_akivymd_sylvia_dynamic.tools'],
    package_data={
        "kivymd_akivymd_sylvia_dynamic": ["icont/*.ttf", "icont/*.fontd"]
    },
    url='https://github.com/kengoon/KivyMD-AKivymd-Sylvia-Dynamic',
    license='MIT',
    author='Akubue Kenechukwu',
    author_email='kengoon19@gmail.com',
    install_requires=["kivy>=1.10.1", "kivymd>=0.104.1", "akivymd"],
    description='This package is a dynamic library that helps you to manipulate kivymd and akivymd to your taste, '
                'it gives you more options to change'
)
