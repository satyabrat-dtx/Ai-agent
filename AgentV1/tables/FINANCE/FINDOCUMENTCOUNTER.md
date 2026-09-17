# DB2ADMIN.FINDOCUMENTCOUNTER

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `DOCUMENTTEMPLATECODE`, `FINANCIALYEARCODE`, `BUSINESSUNITCODE`, `STATISTICALGROUPCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 174737

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `DOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `STATISTICALGROUPCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 8 | `STARTINGNUMBER` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 9 | `LASTUSEDNUMBER` | DECIMAL(10,0) |  |  |  |  |
| 10 | `COUNTERVALUEPOLICYREFCODE` | CHAR(20) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `MONTHPREFIX` | CHAR(3) |  |  |  |  |
| 19 | `RUNNINGCOUNTER` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINDOCUMENTCOUNTER.COMPANYCODE = COMPANY.CODE` |
| `FINDOCUMENTTEMPLATE_DOCUMENTTEMPLATE` | `DOCUMENTTEMPLATECOMPANYCODE`, `DOCUMENTTEMPLATECODE` | [`FINDOCUMENTTEMPLATE`](../FINANCE/FINDOCUMENTTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINDOCUMENTCOUNTER.DOCUMENTTEMPLATECOMPANYCODE = FINDOCUMENTTEMPLATE.COMPANYCODE AND FINDOCUMENTCOUNTER.DOCUMENTTEMPLATECODE = FINDOCUMENTTEMPLATE.CODE` |
| `FINFINANCIALYEAR_FINANCIALYEAR` | `FINANCIALYEARCOMPANYCODE`, `FINANCIALYEARCODE` | [`FINFINANCIALYEAR`](../FINANCE/FINFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINDOCUMENTCOUNTER.FINANCIALYEARCOMPANYCODE = FINFINANCIALYEAR.COMPANYCODE AND FINDOCUMENTCOUNTER.FINANCIALYEARCODE = FINFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINDOCUMENTCOUNTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.BUSINESSUNITCODE,
       t.STATISTICALGROUPCOMPANYCODE,
       t.STATISTICALGROUPCODE,
       t.STARTINGNUMBER,
       t.LASTUSEDNUMBER,
       t.COUNTERVALUEPOLICYREFCODE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.FINDOCUMENTCOUNTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
