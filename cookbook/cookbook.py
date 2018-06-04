from openerp import api, exceptions, fields, models

DIFFICULTIES = [
    ('1', 'soo easy'),
    ('2', 'easy'),
    ('3', 'average'),
    ('4', 'difficult'),
    ('5', 'arduous')]


class RecipeCategory(models.Model):
    _name = 'cookbook.recipe.category'
    _description = 'Recipe categories'
    name = fields.Char(required=True)

    @api.one
    @api.constrains('name')
    def _check_name(self):
        if self.search([('name', '=ilike', self.name), ('id', '!=', self.id)]):
            raise exceptions.ValidationError("The category name must be unique.")


class Cookbook(models.Model):
    _name = 'cookbook.recipe'
    _description = 'Recipes'
    name = fields.Char(required=True)
    category_id = fields.Many2one('cookbook.recipe.category', string='Category')
    is_public = fields.Boolean(default=True)
    difficulty = fields.Selection(DIFFICULTIES, index=True)
    cooking_time = fields.Integer(help="Time in minutes for the preparation")
    baking_time = fields.Integer(help="Time in minutes for the baking")
    ingredients = fields.Html()
    preparation = fields.Html()
    total_time = fields.Integer(compute='_compute_total_time', store=True)

    @api.depends('baking_time', 'cooking_time')
    def _compute_total_time(self):
        for rec in self:
            rec.total_time = rec.cooking_time + rec.baking_time






