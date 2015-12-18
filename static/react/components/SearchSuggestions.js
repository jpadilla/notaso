import React from 'react';
import Radium from 'radium';

const styles = {
  box: {
    position: 'absolute',
    top: '35px',
    left: '16px',
    right: '16px',
    zIndex: '10',
    paddingTop: '0',
    marginTop: '7px',
    boxShadow: '0 2px 5px #777'
  },
  item: {
    padding: '5px 10px',
    backgroundColor: 'white',
    ':hover': {
      cursor: 'pointer',
      backgroundColor: '#EEE'
    }
  },
  text: {
    margin: '0'
  },
  name: {
    color: '#333'
  },
  university: {
    color: '#999',
    fontSize: '12px'
  },
  link: {
    textDecoration: 'none',
    display: 'block',
    width: '100%',
    height: '100%'
  },
  list: {
    marginBottom: '0'
  }
};

class SearchSuggestions extends React.Component {
  render() {
    const view = (this.props.suggestions.length > 0) ? (
      <div style={styles.box}>
        <ul style={styles.list}>
          {this.props.suggestions.map(item=> {
            const url = `/professors/${item.slug}/`;
            return (
              <li style={styles.item} key={item.id}>
                <a style={styles.link} href={url} key={item.id}>
                  <p style={[styles.text, styles.name]}>{item.first_name} {item.last_name}</p>
                  <p style={[styles.text, styles.university]}>{item.university}</p>
                </a>
              </li>
            );
          })}
        </ul>
      </div>
    ) : (<div></div>);
    return view;
  }
}

export default Radium(SearchSuggestions);