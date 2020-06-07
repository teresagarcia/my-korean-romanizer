from distutils.core import setup
setup(
  name = 'mykoreanromanizer',         
  packages = ['mykoreanromanizer'],   
  version = '0.1',     
  license='MIT',      
  description = 'Custom Korean romanizer',   
  author = 'Teresa García',                   
  author_email = 'teresagar181@gmail.com',    
  url = 'https://github.com/teresagarcia/my-korean-romanizer',   
  download_url = 'https://github.com/teresagarcia/my-korean-romanizer/archive/v_01.tar.gz',    
  keywords = ['Korean', 'Romanizer'],   
  install_requires=[            
          'jamo'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',    
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)