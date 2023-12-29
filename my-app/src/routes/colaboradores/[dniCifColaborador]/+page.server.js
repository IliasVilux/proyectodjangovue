export function load({params}){
    return params.dniCifColaborador ? {dniCifColaborador: params.dniCifColaborador} : null;
}