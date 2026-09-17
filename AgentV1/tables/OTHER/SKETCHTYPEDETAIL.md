# DB2ADMIN.SKETCHTYPEDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 207379

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `BASEUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `ITEMOFCLOTHINGCODE` | CHAR(10) |  | FK | foreign_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SKETCHTYPE_ITEMOFCLOTHING` | `COMPANYCODE`, `ITEMOFCLOTHINGCODE` | [`SKETCHTYPE`](../OTHER/SKETCHTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SKETCHTYPEDETAIL.COMPANYCODE = SKETCHTYPE.COMPANYCODE AND SKETCHTYPEDETAIL.ITEMOFCLOTHINGCODE = SKETCHTYPE.CODE` |
| `UNITOFMEASURE_BASEUOM` | `BASEUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SKETCHTYPEDETAIL.BASEUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SKETCHTYPEDETAIL_SKETCHTYPEDETAIL` | [`SKETCHTEMPLATEDETAIL`](../OTHER/SKETCHTEMPLATEDETAIL.md) | `SKETCHTEMPLATECOMPANYCODE`, `SKETCHTYPEDETAILCODE` | `SKETCHTEMPLATEDETAIL.SKETCHTEMPLATECOMPANYCODE = SKETCHTYPEDETAIL.COMPANYCODE AND SKETCHTEMPLATEDETAIL.SKETCHTYPEDETAILCODE = SKETCHTYPEDETAIL.CODE` |

## Indexes

- `SKETCHTYPEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.BASEUOMCODE,
       t.ITEMOFCLOTHINGCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SKETCHTYPEDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
