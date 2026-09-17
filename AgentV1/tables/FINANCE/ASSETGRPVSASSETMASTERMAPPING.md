# DB2ADMIN.ASSETGRPVSASSETMASTERMAPPING

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `MAINASSETASSETUGENGRPTYPECODE`, `MAINASSETASSETCODE`, `MAINASSETCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239452

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MAINASSETASSETUGENGRPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `MAINASSETASSETCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `MAINASSETCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `AGUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `AGUSERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `AGCODE` | CHAR(10) |  | FK | foreign_key |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ASSETGRPVSASSETMASTERMAPPING.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ASSETGRPVSASSETMASTERMAPPING.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND ASSETGRPVSASSETMASTERMAPPING.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `USERGENERICGROUP_AG` | `AGUGENGROUPTYPECOMPANYCODE`, `AGUSERGENERICGROUPTYPECODE`, `AGCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `ASSETGRPVSASSETMASTERMAPPING.AGUGENGROUPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND ASSETGRPVSASSETMASTERMAPPING.AGUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND ASSETGRPVSASSETMASTERMAPPING.AGCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ASSETGRPVSASSETMMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.MAINASSETASSETUGENGRPTYPECODE,
       t.MAINASSETASSETCODE,
       t.MAINASSETCODE,
       t.AGUGENGROUPTYPECOMPANYCODE,
       t.AGUSERGENERICGROUPTYPECODE,
       t.AGCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ASSETGRPVSASSETMASTERMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
