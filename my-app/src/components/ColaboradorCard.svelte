<script>
	import DeleteButton from './DeleteButton.svelte';
	import { queryStore, getContextClient, gql } from '@urql/svelte';

	export let dni;
	const client = getContextClient();

	const colaborador = queryStore({
		client: client,
		query: gql`
			query colaborador($dniCifColaborador: String!) {
				colaborador(dniCifColaborador: $dniCifColaborador) {
					dniCifColaborador
					nombreColaborador
					apellidosColaborador
				}
			}
		`,
		variables: { dniCifColaborador: dni }
	});
</script>

{#if $colaborador.fetching}
	<p>Loading...</p>
{:else if $colaborador.error}
	<p>Oh no... {$colaborador.error.message}</p>
{:else}
	<div class="card">
		<a class="btn" href="colaboradores/{$colaborador.data.colaborador.dniCifColaborador}">
			{$colaborador.data.colaborador.nombreColaborador}
			{#if $colaborador.data.colaborador.apellidosColaborador}
				{$colaborador.data.colaborador.apellidosColaborador}
			{/if}
		</a>
		<DeleteButton on:clicked />
	</div>
{/if}

<style>
	.card {
		display: flex;
		align-items: center;
		box-shadow:
			rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
			rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
		height: 100px;
		margin: 20px 0;
		vertical-align: middle;
		padding: 10px;
		text-transform: capitalize;
		border-radius: 10px;
	}
</style>
