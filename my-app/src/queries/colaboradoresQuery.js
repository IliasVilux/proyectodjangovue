import { gql } from '@apollo/client/core';

export const GET_COLABORADORES = gql`
	query allColaboradores {
		colaboradores {
			dniCifColaborador
			nombreColaborador
		}
	}
`;

export const GET_COLABORADOR = gql`
	query colaborador($dniCifColaborador: String!) {
		colaborador(dniCifColaborador: $dniCifColaborador) {
			dniCifColaborador
			nombreColaborador
		}
	}
`;

export const ADD_COLABORADOR = gql`
	mutation addColaborador($dniCifColaborador: String!, $nombreColaborador: String!) {
		addColaborador(dniCifColaborador: $dniCifColaborador, nombreColaborador: $nombreColaborador) {
			colaborador {
				dniCifColaborador
				nombreColaborador
			}
		}
	}
`;

export const UPDATE_COLABORADOR = gql`
	mutation updateColaborador($dniCifColaborador: String!, $nombreColaborador: String!) {
		updateColaborador(
			dniCifColaborador: $dniCifColaborador
			nombreColaborador: $nombreColaborador
		) {
			colaborador {
				dniCifColaborador
				nombreColaborador
			}
		}
	}
`;

export const DELETE_COLABORADOR = gql`
	mutation deleteColaborador($dniCifColaborador: String!) {
		deleteColaborador(dniCifColaborador: $dniCifColaborador) {
			colaborador {
				dniCifColaborador
				nombreColaborador
			}
		}
	}
`;
