import React from 'react';
import SearchSuggestions from './SearchSuggestions';

export default class Search extends React.Component {
  constructor() {
    super();
    this.state = {
      searchText: '',
      professors: []
    }
  }
  handleChange() {
    const text = this.refs.searchBox.value;
    this.setState({
      searchText: text
    });
    if (text.length > 2) {
      $.get(`/api/v2/professors/?search=${encodeURIComponent(text)}`, (resp)=> {
        const data = resp.results.sort((a, b)=> {
          const nameA = `${a.first_name} ${a.last_name}`.toLowerCase();
          const nameB = `${b.first_name} ${b.last_name}`.toLowerCase();

          if (nameA.indexOf(text.toLowerCase()) < nameB.indexOf(text.toLowerCase()))
            return -1;
          if (nameA.indexOf(text.toLowerCase()) > nameB.indexOf(text.toLowerCase()))
            return 1;
          return 0;
        }).slice(0, 8);

        if (this.state.searchText.length > 2) {
          this.setState({
            professors: data
          });
        } else {
          this.setState({
            professors: []
          });
        }
      });
    } else {
      this.setState({
        professors: []
      });
    }
  }
  goToSearchPage() {
    window.location = `/search/?q=${encodeURIComponent(this.state.searchText)}`;
  }
  render() {
    return (
      <div className='navbar-form'>
        <div className='input-group'>
          <input
            ref='searchBox'
            type='text'
            className='search-text form-control'
            placeholder='Busca un profesor'
            value={this.state.searchText}
            onChange={::this.handleChange}/>
          <span className='input-group-btn'>
            <button
              className='btn btn-default'
              onClick={::this.goToSearchPage}>
              <span className='glyphicon glyphicon-search'></span>
            </button>
          </span>
        </div>
        <SearchSuggestions suggestions={this.state.professors}/>
      </div>
    );
  }
}