// blockchain/contrato.sol
pragma solidity ^0.8.0;

contract PermisosTrabajo {
    struct Permiso {
        string trabajador;
        string descripcion;
        uint fecha;
    }

    Permiso[] public permisos;

    function crearPermiso(string memory _trabajador, string memory _descripcion) public {
        permisos.push(Permiso(_trabajador, _descripcion, block.timestamp));
    }

    function obtenerPermisos() public view returns (Permiso[] memory) {
        return permisos;
    }
}
