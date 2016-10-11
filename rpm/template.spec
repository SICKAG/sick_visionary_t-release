Name:           ros-indigo-sick-visionary-t-driver
Version:        0.0.3
Release:        1%{?dist}
Summary:        ROS sick_visionary_t_driver package

Group:          Development/Libraries
License:        Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
URL:            http://wiki.ros.org/sick_visionary_t_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-sensor-msgs

%description
Open source driver for the SICK Visionary-T 3D TOF camera.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Oct 11 2016 Joshua Hampp <joshua.hampp@ipa.fraunhofer.de> - 0.0.3-1
- Autogenerated by Bloom

* Tue Oct 11 2016 Joshua Hampp <joshua.hampp@ipa.fraunhofer.de> - 0.0.3-0
- Autogenerated by Bloom

* Fri Oct 07 2016 Joshua Hampp <joshua.hampp@ipa.fraunhofer.de> - 0.0.2-0
- Autogenerated by Bloom

