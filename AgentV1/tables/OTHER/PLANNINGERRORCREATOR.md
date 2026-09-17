# DB2ADMIN.PLANNINGERRORCREATOR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31167

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `GBPARAMETERS` | LONG VARCHAR |  |  |  |  |
| 5 | `GROUPNUMBER` | BIGINT | NOT NULL |  |  |  |
| 6 | `LINENUMBER` | INTEGER | NOT NULL |  |  |  |
| 7 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `REQUISITIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `ENTITYTYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.GBPARAMETERS,
       t.GROUPNUMBER,
       t.LINENUMBER,
       t.CODE,
       t.COUNTERCODE,
       t.REQUISITIONTEMPLATECODE,
       t.ENTITYTYPE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PLANNINGERRORCREATOR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
