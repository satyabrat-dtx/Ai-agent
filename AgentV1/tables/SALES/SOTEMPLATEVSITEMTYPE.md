# DB2ADMIN.SOTEMPLATEVSITEMTYPE

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `ANALYSISCODE`, `SOTEMPLATECODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125445

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ANALYSISCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SOTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ANALYSISTYPE_ANALYSIS` | `COMPANYCODE`, `ANALYSISCODE` | [`ANALYSISTYPE`](../ITEM_MASTER/ANALYSISTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SOTEMPLATEVSITEMTYPE.COMPANYCODE = ANALYSISTYPE.COMPANYCODE AND SOTEMPLATEVSITEMTYPE.ANALYSISCODE = ANALYSISTYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SOTEMPLATEVSITEMTYPE.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SOTEMPLATEVSITEMTYPE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND SOTEMPLATEVSITEMTYPE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `SALESORDERTEMPLATE_SOTEMPLATE` | `COMPANYCODE`, `SOTEMPLATECODE` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SOTEMPLATEVSITEMTYPE.COMPANYCODE = SALESORDERTEMPLATE.COMPANYCODE AND SOTEMPLATEVSITEMTYPE.SOTEMPLATECODE = SALESORDERTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SOTEMPLATEVSITEMTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ANALYSISCODE,
       t.SOTEMPLATECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SOTEMPLATEVSITEMTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
