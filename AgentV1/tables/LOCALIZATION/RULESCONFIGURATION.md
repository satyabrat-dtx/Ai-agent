# DB2ADMIN.RULESCONFIGURATION

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `COMPITEMTYPECODE`, `COMBINATIONTYPE`, `RULETEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130567

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COMPITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `COMPITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `COMBINATIONTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `RULETEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RULESCONFIGURATION.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_COMPITEMTYPE` | `COMPITEMTYPECOMPANYCODE`, `COMPITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULESCONFIGURATION.COMPITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND RULESCONFIGURATION.COMPITEMTYPECODE = ITEMTYPE.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULESCONFIGURATION.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND RULESCONFIGURATION.ITEMTYPECODE = ITEMTYPE.CODE` |
| `RULETEMPLATEHEADER_RULETEMPLATE` | `COMPANYCODE`, `RULETEMPLATECODE` | [`RULETEMPLATEHEADER`](../LOCALIZATION/RULETEMPLATEHEADER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULESCONFIGURATION.COMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULESCONFIGURATION.RULETEMPLATECODE = RULETEMPLATEHEADER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RULESCONFIGURATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.COMPITEMTYPECOMPANYCODE,
       t.COMPITEMTYPECODE,
       t.COMBINATIONTYPE,
       t.RULETEMPLATECODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.RULESCONFIGURATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
