export function load({params}){
    return params.dniCifColaborador ? {dniCifColaborador: params.dniCifColaborador} : null;
}

export const actions = {
	create: () => {},
	update: () => {}
};