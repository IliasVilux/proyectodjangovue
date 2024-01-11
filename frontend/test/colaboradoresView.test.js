import { beforeEach, describe, expect, test } from 'vitest'
import { GET_COLABORADORES, GET_COLABORADOR } from '@/graphql/Queries/Colaboradores'
import ColaboradorCard from '@/components/ColaboradorCard.vue'
import UpdateColaboradorButton from '@/components/UpdateColaboradorButton.vue'
import DeleteColaboradorButton from '@/components/DeleteColaboradorButton.vue'
import { mount, RouterLinkStub, shallowMount } from '@vue/test-utils'
import { provideApolloClient } from '@vue/apollo-composable'
import { apolloClient } from '@/main'

provideApolloClient(apolloClient)

describe('ApolloGQL queries and mutations', () => {
  test('all colaboradores query get data', () => {
    expect(GET_COLABORADORES).toBeDefined()
  })
  test('colaborador query get data', () => {
    expect(GET_COLABORADOR).toBeDefined()
  })
})

describe('ColaboradorCard.vue', () => {
  const mocks = [
    {
      request: {
        query: GET_COLABORADOR,
        variables: {
          dniCifColaborador: '47695734B'
        }
      },
      result: {
        data: {
          colaborador: { dniCifColaborador: '47695734B', nombreColaborador: 'BlackOps' }
        }
      }
    }
  ]

  let wrapper = null
  beforeEach(async () => {
    wrapper = mount(ColaboradorCard, {
      props: {
        dni: '47695734B'
      }
    })

    // wrapper.setData({
    //   result: mock[0].result
    // })
  })

  test.only('mount component', () => {
    console.log(wrapper.html())
    expect(ColaboradorCard).toBeTruthy()
    expect(wrapper.props('dni')).toBe('47695734B')
  })
})

describe('UpdateColaboradorButton.vue', () => {
  let wrapper = null
  beforeEach(() => {
    wrapper = shallowMount(UpdateColaboradorButton, {
      props: {
        dniCifColaborador: '47695734B'
      },
      global: {
        stubs: {
          RouterLink: RouterLinkStub
        }
      }
    })
  })

  test('mount component', () => {
    expect(UpdateColaboradorButton).toBeTruthy()
    expect(wrapper.props('dniCifColaborador')).toBe('47695734B')
  })

  test('navigates to form with the dniCifColaborador', () => {
    expect(wrapper.findComponent(RouterLinkStub).props('to')).toEqual({
      name: 'formcolaborador',
      params: {
        dniCifColaborador: '47695734B'
      }
    })
  })
})

describe('DeleteColaboradorButton.vue', () => {
  let wrapper = null
  beforeEach(() => {
    wrapper = shallowMount(DeleteColaboradorButton)
  })

  test('mount component', () => {
    expect(DeleteColaboradorButton).toBeTruthy()
  })

  test('emit delete on click', () => {
    wrapper.find('.deleteBtn').trigger('click')
    expect(wrapper.emitted().delete).toBeTruthy()
  })
})
