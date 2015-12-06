%global modname portalocker

%global commit b0de666bb7d67289cb39af5d28dcf749ad9d8d50
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        0.5.4
Release:        1.git%{shortcommit}%{?dist}
Summary:        Library to provide an easy API to file locking

License:        Python
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://github.com/WoLpH/portalocker/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  python2-pytest

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}

sed -i -e '/--/d' pytest.ini

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{modname}
%license LICENSE
%doc CHANGELOG README.rst
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc CHANGELOG README.rst
%{python3_sitelib}/%{modname}*

%changelog
* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5.4-1.gitb0de666
- Initial package
