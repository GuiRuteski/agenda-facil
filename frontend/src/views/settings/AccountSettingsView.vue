<template>
  <div :class="styles['accountsettings-container']">
    <!-- Barra lateral (sidebar) -->
    <aside :class="styles['accountsettings-sidebar']">
      <div :class="styles['accountsettings-logo-box']">
        <img 
          :src="require('../../assets/logo.png')" 
          alt="Logo Agenda Fácil" 
          :class="styles['accountsettings-logo']" 
        />
      </div>

      <ul :class="styles['accountsettings-menu-list']">
        <li 
          v-for="item in menuItems" 
          :key="item.label" 
          :class="[styles['accountsettings-menu-item'], activeMenu === item.label ? styles['accountsettings-active-menu'] : '']"
          role="button"
          tabindex="0"
          @click="handleMenuClick(item.label)"
        >
          <i :class="[item.icon]" style="margin-right: 10px;"></i>
          {{ item.label }}
        </li>
      </ul>
    </aside>

    <!-- Conteúdo principal da página -->
    <main :class="styles['accountsettings-main-content']">
      <div :class="styles['accountsettings-header-row']">
        <div :class="styles['accountsettings-top-bar']">
          <div :class="styles['accountsettings-user-info']">
            <h1>Olá, Sr. {{ userName }}!</h1>
            <div :class="styles['accountsettings-user-underline-box']">
              <div :class="[styles['accountsettings-user-underline'], styles.short]"></div>
              <div :class="[styles['accountsettings-user-underline'], styles.long]"></div>
            </div>
          </div>
          <img 
            :src="userPhoto"
            @error="userPhoto = require('../../assets/User.jpg')"
            alt="Foto do usuário" 
            :class="styles['accountsettings-user-photo']" 
          />
        </div>     
      </div>

      <!-- Seção do formulário e foto -->
      <section :class="styles['accountsettings-form-section']">
        <div :class="styles['accountsettings-form-box']">
          <label for="name">Nome</label>
          <input id="name" v-model="form.name" type="text" :disabled="!isEditing" />

          <label for="email">E-Mail</label>
          <input id="email" v-model="form.email" type="email" :disabled="!isEditing" />

          <label for="language">Idioma</label>
          <select id="language" v-model="form.language" :disabled="!isEditing">
            <option>Português (Brasil)</option>
            <option>English (US)</option>
            <option>Español</option>
          </select>

          <label for="password">Senha</label>
          <input id="password" v-model="form.password" type="password" :disabled="!isEditing" />

          <div :class="styles['accountsettings-form-buttons']">
            <template v-if="!isEditing">
              <button 
                :class="styles['btn-delete']"
                @click="handleDelete"
              >EXCLUIR</button>

              <button 
                :class="styles['btn-edit']"
                @click="toggleEdit"
              >EDITAR</button>
            </template>

            <template v-else>
              <button 
                :class="styles['btn-cancel']"
                @click="cancelEdit"
              >CANCELAR</button>

              <button 
                :class="styles['btn-save']"
                @click="toggleEdit"
              >SALVAR</button>
            </template>
          </div>
        </div>

        <div :class="styles['accountsettings-photo-box']">
          <img 
            :src="userPhoto" 
            alt="Foto do usuário" 
            :class="styles['accountsettings-photo-preview']" 
          />
          <button :class="styles['btn-alter']">ALTERAR</button>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import styles from '@/assets/css/AccountSettingsView.module.css';

export default {
  data() {
    return {
      styles,
      userName: 'Marcos',
      userPhoto: require('../../assets/User.jpg'),
      menuItems: [
        { label: 'INÍCIO', icon: 'fas fa-home' },
        { label: 'CONSULTAS', icon: 'fas fa-calendar-check' },
        { label: 'PROFISSIONAIS', icon: 'fas fa-user-md' },
        { label: 'PACIENTE', icon: 'fas fa-user' },
        { label: 'MENSAGENS', icon: 'fas fa-comments' },
        { label: 'CONFIGURAÇÕES', icon: 'fas fa-cog' },
        { label: 'SAIR', icon: 'fas fa-sign-out-alt' }
      ],
      activeMenu: 'CONFIGURAÇÕES',
      isEditing: false,
      form: {
        name: 'Marcos Oliveira Souza',
        email: 'marcos@gmail.com',
        language: 'Português (Brasil)',
        password: '**********'
      },
      originalForm: {}
    };
  },
  mounted() {
    this.originalForm = { ...this.form };
  },
  methods: {
    handleMenuClick(label) {
      this.activeMenu = label;
      switch (label) {
        case 'INÍCIO':
          this.$router.push('/home');
          break;
        case 'CONSULTAS':
          this.$router.push('/scheduling');
          break;
        case 'PROFISSIONAIS':
          this.$router.push('/professional');
          break;
        case 'PACIENTE':
          this.$router.push('/patient');
          break;
        case 'MENSAGENS':
          this.$router.push('/message');
          break;
        case 'CONFIGURAÇÕES':
          this.$router.push('/settings');
          break;
        case 'SAIR':
          this.logout();
          break;
      }
    },
    logout() {
      this.$router.push('/login');
    },
    toggleEdit() {
      if (this.isEditing) {
        this.originalForm = { ...this.form };
        this.isEditing = false;
      } else {
        this.isEditing = true;
      }
    },
    cancelEdit() {
      this.form = { ...this.originalForm };
      this.isEditing = false;
    },
    handleDelete() {
      alert('Função de exclusão ainda não implementada.');
    }
  }
};
</script>
