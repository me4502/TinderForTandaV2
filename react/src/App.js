import React, {Component} from 'react';
import {Button, Checkbox, Form, Header} from 'semantic-ui-react'
import SuperAgent from 'superagent';

class App extends Component {
  render() {
    return (
      <Form>
        <Header size='huge'>Sign in with Facebook</Header>
        <p>
          Tinder for Tanda requires your real Facebook username and password to scrape
          your information, and create sick integrations in your workplace. :)
        </p>
        <Form.Field>
          <label>Email</label>
          <input placeholder='Email' type="email"/>
        </Form.Field>
        <Form.Field>
          <label>Password</label>
          <input placeholder='Password' type="password"/>
        </Form.Field>
        <Form.Field>
          <Checkbox label='I agree to the Terms and Conditions'/>
        </Form.Field>
        <Button type='submit'>Submit</Button>
      </Form>
    );
  }
}

export default App;
