# Maintainer: Einar Arnason <einar@mikro.solutions>
pkgname=python-DateVersioning
pkgver=20.292.114220
pkgrel=1
epoch=
pkgdesc="Print git commit dates in version format"
arch=('any')
url="https://github.com/EinarArnason/DateVersioning.git"
license=('None')
groups=()
depends=(python)
makedepends=(python python-setuptools)
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=()
noextract=()
md5sums=()
validpgpkeys=()

pkgver() {
    cd ${srcdir}/../
    python setup.py -V
}

build() {
    cd ${srcdir}/../
    python setup.py build
}

check() {
    cd ${srcdir}/../
    python -m unittest discover -v -s tests -p *_test.py
}

package() {
    cd ${srcdir}/../
    python setup.py install --prefix=/usr --root="$pkgdir" --optimize=1 --skip-build
}