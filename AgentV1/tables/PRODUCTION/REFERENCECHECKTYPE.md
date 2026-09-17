# DB2ADMIN.REFERENCECHECKTYPE

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 2 of 2 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `CODE`
- **FK degree**: referenced by 4 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30993

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `UIDEFPATH` | VARCHAR(50) |  |  |  |  |
| 5 | `UIDEFNAME` | VARCHAR(54) |  |  |  |  |
| 6 | `CODETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `CODELENGTH` | INTEGER | NOT NULL |  |  |  |
| 8 | `COMPANYNAMEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ITEMTYPENAMEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `OTHERPARAMETERS` | CLOB(1000000) |  |  |  |  |
| 11 | `CHECKREFERENCECODE` | CHAR(20) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `REFERENCECHECKTYPE_CHECK` | [`ROUTINGANALYSISREPORT`](../PRODUCTION/ROUTINGANALYSISREPORT.md) | `CHECKCODE` | `ROUTINGANALYSISREPORT.CHECKCODE = REFERENCECHECKTYPE.CODE` |
| `REFERENCECHECKTYPE_CHECK` | [`RECIPETEMPLATE`](../OTHER/RECIPETEMPLATE.md) | `CHECKCODE` | `RECIPETEMPLATE.CHECKCODE = REFERENCECHECKTYPE.CODE` |
| `REFERENCECHECKTYPE_CHECK` | [`BILLOFMATERIAL`](../CORE_MASTER/BILLOFMATERIAL.md) | `CHECKCODE` | `BILLOFMATERIAL.CHECKCODE = REFERENCECHECKTYPE.CODE` |
| `REFERENCECHECKTYPE_CHECK` | [`ROUTING`](../PRODUCTION/ROUTING.md) | `CHECKCODE` | `ROUTING.CHECKCODE = REFERENCECHECKTYPE.CODE` |

## Indexes

- `REFERENCECHECKTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.UIDEFPATH,
       t.UIDEFNAME,
       t.CODETYPE,
       t.CODELENGTH,
       t.COMPANYNAMEREQUIRED,
       t.ITEMTYPENAMEREQUIRED,
       t.OTHERPARAMETERS,
       t.CHECKREFERENCECODE
FROM   DB2ADMIN.REFERENCECHECKTYPE t
FETCH FIRST 100 ROWS ONLY;
```
