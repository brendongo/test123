class Foo
  route :post, '/api/foo' do
    File.join(File.dirname(path), "foo_#{File.basename(path)}")
    api_ok {}
  end
end