<script>
	import { query, mutation } from 'svelte-apollo';
	import { gql } from '@apollo/client/core';
	import ColaboradorCard from '../../components/ColaboradorCard.svelte';
	import { GET_COLABORADORES, DELETE_COLABORADOR } from '../../queries/colaboradoresQuery';

	const colaboradores = query(GET_COLABORADORES);
	const deleteColaborador = mutation(DELETE_COLABORADOR);

	const deleteClick = (dniCifColaborador) => {
		deleteColaborador(
			{ variables: { dniCifColaborador },
			refetchQueries: ['allColaboradores']
		 });
	};
</script>

<div class="container">
	<h1>colaboradores</h1>

	<a href="colaboradores/añadir" class="btn">Agregar Nuevo Colaborador</a>

	{#if $colaboradores.loading}
		<p>Loading...</p>
	{:else if $colaboradores.error}
		<p>Oh no... {$colaboradores.error.message}</p>
	{:else}
		<ul style="padding: 0; margin-top: 2rem;">
			{#each $colaboradores.data.colaboradores as colaborador (colaborador.dniCifColaborador)}
				<ColaboradorCard
					dni={colaborador.dniCifColaborador}
					on:clicked={deleteClick(colaborador.dniCifColaborador)}
				/>
			{/each}
		</ul>
	{/if}
</div>

<style>
	.container {
		width: 45%;
		margin: auto;
	}
	.btn {
		background-color: #020d19;
		color: #e0e0e0;
		padding: 10px;
		border-radius: 10px;
	}
	h1 {
		text-align: center;
		text-transform: uppercase;
		margin-bottom: 4rem;
	}
</style>
