FROM python:3.7

COPY netCDF4-1.5.3.tar.gz netCDF4-1.5.3.tar.gz
COPY proj-7.0.1.tar.gz proj-7.0.1.tar.gz
COPY geos-3.8.1.tar.bz2 geos-3.8.1.tar.bz2

RUN apt-get update && \
    apt-get upgrade -y && \
	apt-get -yq install build-essential tar m4 zlib1g-dev libopenmpi-dev hdf5-tools hdf5-helpers libhdf5-dev libhdf5-doc libhdf5-serial-dev libnetcdf-dev libnetcdff-dev libgeos-dev sqlite3 bzip2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
	tar xzf proj-7.0.1.tar.gz && \
	cd proj-7.0.1 && \
	./configure && \
	make && \
	make install && \
	cd / && \
    tar xjf geos-3.8.1.tar.bz2 && \
	cd geos-3.8.1 && \
	./configure --enable-python && \
	make && \
	make install && \
	cd / && \
    pip install --upgrade pip && \
    pip install numpy matplotlib cython jupyter h5py pyshp six scipy iris && \
	pip install shapely --no-binary shapely && \
	pip install cartopy && \
	tar xzf netCDF4-1.5.3.tar.gz && \
	cd  netCDF4-1.5.3 && \
	python setup.py build && \
    python setup.py install && \
	rm -rf /netCDF4-1.5.3 /net4-1.5.3.tar.gz /proj-7.0.1 /proj-7.0.1.tar.gz /geos-3.8.1 /geos-3.8.1.tar.bz2

CMD jupyter notebook --no-browser
