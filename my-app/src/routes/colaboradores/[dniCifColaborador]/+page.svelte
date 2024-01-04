<script>
	import { mutation, query } from 'svelte-apollo';
	import { gql } from '@apollo/client/core';
	import { goto } from '$app/navigation';
	import {
		GET_COLABORADOR,
		ADD_COLABORADOR,
		UPDATE_COLABORADOR
	} from '../../../queries/colaboradoresQuery';

	export let data;
	let dataGetted = false;
	$: form = {
		dniCifColaborador: '',
		nombreColaborador: ''
	};

	const colaborador = query(GET_COLABORADOR, {
		variables: { dniCifColaborador: data.dniCifColaborador }
	});

	$: if (!dataGetted && $colaborador.data && $colaborador.data.colaborador) {
		form.dniCifColaborador = $colaborador.data.colaborador.dniCifColaborador;
		form.nombreColaborador = $colaborador.data.colaborador.nombreColaborador;
		dataGetted = true;
	}

	const addColaborador = mutation(ADD_COLABORADOR);
	const updateColaborador = mutation(UPDATE_COLABORADOR);

	function handleSubmit() {
		if (data.dniCifColaborador === 'añadir') {
			addColaborador({
				variables: {
					dniCifColaborador: form.dniCifColaborador,
					nombreColaborador: form.nombreColaborador
				},
				update(cache, { data: { addColaborador } }) {
					cache.modify({
						fields: {
							colaboradores(existingColaboradores = []) {
								const newColaboradorRef = cache.writeFragment({
									data: addColaborador.colaborador,
									fragment: gql`
										fragment NewColaborador on Colaborador {
											dniCifColaborador
											type
										}
									`
								});
								return [...existingColaboradores, newColaboradorRef];
							}
						}
					});
				}
			});
		} else {
			updateColaborador({
				variables: {
					dniCifColaborador: form.dniCifColaborador,
					nombreColaborador: form.nombreColaborador
				}
			});
		}
		goto('/colaboradores');
	}
</script>

<form on:submit|preventDefault={handleSubmit}>
	<input type="text" name="dni" bind:value={form.dniCifColaborador} />
	<input type="text" name="name" bind:value={form.nombreColaborador} />
	<button type="submit" disabled={form.dniCifColaborador.length < 1}>
		{data.dniCifColaborador === 'añadir' ? 'Crear' : 'Modificar'}
	</button>
</form>
