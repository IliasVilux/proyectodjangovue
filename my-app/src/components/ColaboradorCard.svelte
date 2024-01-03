<script>
	import { query } from 'svelte-apollo';
	import DeleteButton from "./DeleteButton.svelte";
	import { GET_COLABORADOR } from '../queries/colaboradoresQuery';

	export let dni

	const colaborador = query(GET_COLABORADOR,
	{ variables: {dniCifColaborador: dni} });
</script>

{#if $colaborador.loading}
	<p>Loading...</p>
{:else if $colaborador.error}
	<p>Oh no... {$colaborador.error.message}</p>
{:else}
	<div class="card">
		<a class="btn" href="colaboradores/{$colaborador.data.colaborador.dniCifColaborador}">
			{$colaborador.data.colaborador.nombreColaborador}
		</a>
		<DeleteButton on:clicked />
	</div>
{/if}

<style>
	.card {
		display: flex;
		align-items: center;
		justify-content: space-between;
		box-shadow:
			rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
			rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
		height: 100px;
		margin: 10px 0;
		vertical-align: middle;
		padding: 10px 30px;
		text-transform: capitalize;
		border-radius: 10px;
	}
</style>
