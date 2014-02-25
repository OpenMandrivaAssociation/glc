%define major 0
%define libcapture %mklibname %{name}-capture %{major}
%define libcore %mklibname %{name}-core %{major}
%define libexport %mklibname %{name}-export %{major}
%define libhook %mklibname %{name}-hook %{major}
%define libplay %mklibname %{name}-play %{major}
%define devname %mklibname %{name} -d

Summary:	ALSA and OpenGL video capture tool
Name:		glc
Version:	0.5.8
Release:	2
License:	MIT
Group:		Video
Url:		https://github.com/nullkey/glc
Source0:	https://nodeload.github.com/nullkey/glc/tarball/master/%{name}-%{version}.tar.bz2
Patch0:		glc-0.5.8-alsa-capture-stop.patch
Patch1:		glc-0.5.8-linkage.patch
BuildRequires:	cmake
BuildRequires:	libelfhacks-devel
BuildRequires:	libpacketstream-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xorg-server)

%description
glc is an ALSA and OpenGL video capture tool that you can use to record
the output from opengl applications.

%files -n %{name}
%{_bindir}/glc*

#----------------------------------------------------------------------------

%package -n %{libcapture}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}glc < 0.5.8-2

%description -n %{libcapture}
This project provides a client library for %{name}.

%files -n %{libcapture}
%{_libdir}/lib%{name}-capture.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libcore}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}glc < 0.5.8-2
Obsoletes:	%{_lib}glc < 0.5.8-2

%description -n %{libcore}
This project provides a client library for %{name}.

%files -n %{libcore}
%{_libdir}/lib%{name}-core.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libexport}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}glc < 0.5.8-2

%description -n %{libexport}
This project provides a client library for %{name}.

%files -n %{libexport}
%{_libdir}/lib%{name}-export.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libhook}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}glc < 0.5.8-2

%description -n %{libhook}
This project provides a client library for %{name}.

%files -n %{libhook}
%{_libdir}/lib%{name}-hook.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libplay}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}glc < 0.5.8-2

%description -n %{libplay}
This project provides a client library for %{name}.

%files -n %{libplay}
%{_libdir}/lib%{name}-play.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libcapture} = %{EVRD}
Requires:	%{libcore} = %{EVRD}
Requires:	%{libexport} = %{EVRD}
Requires:	%{libhook} = %{EVRD}
Conflicts:	%{_lib}glc < 0.5.8-2

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -n %{devname}
%{_libdir}/lib%{name}-*.so
%{_includedir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake -DMLIBDIR=%{_lib}
%make

%install
%makeinstall_std -C build

