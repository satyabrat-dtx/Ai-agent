# DB2ADMIN.ABSUIPROCESSUSERPREF

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ABSUIPROCESSCODE`, `COMPANYCODE`, `USERUSERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 49729

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIPROCESSCODE` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `WIDTH` | INTEGER | NOT NULL |  |  |  |
| 4 | `HEIGHT` | INTEGER | NOT NULL |  |  |  |
| 5 | `POSX` | INTEGER | NOT NULL |  |  |  |
| 6 | `POSY` | INTEGER | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUIPROCESS_USERPREF` | `ABSUIPROCESSCODE` | [`ABSUIPROCESS`](../PLATFORM/ABSUIPROCESS.md) | `CODE` | RESTRICT | `ABSUIPROCESSUSERPREF.ABSUIPROCESSCODE = ABSUIPROCESS.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIPROCESSUSERPREFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIPROCESSCODE,
       t.COMPANYCODE,
       t.USERUSERID,
       t.WIDTH,
       t.HEIGHT,
       t.POSX,
       t.POSY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUIPROCESSUSERPREF t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
