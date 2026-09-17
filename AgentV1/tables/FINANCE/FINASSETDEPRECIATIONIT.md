# DB2ADMIN.FINASSETDEPRECIATIONIT

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `FINBUSINESSUNITCODE`, `FINASSETCOUNTERCODE`, `FINASSETCODE`, `FINYEARTODATE`, `ADDITIONALFLAG`, `FINMAINASSETBUSINESSUNITCODE`, `FINMAINASSETASSETUGENGRPTECOD`, `FINMAINASSETASSETCODE`, `FINMAINASSETCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178955

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINBUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINASSETCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINASSETCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `FINYEARTODATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `ADDITIONALFLAG` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 6 | `FINMAINASSETBUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `FINMAINASSETASSETUGENGRPTECOD` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `FINMAINASSETASSETCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `FINMAINASSETCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 10 | `DEPRECIATIONAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINASSETDEPRECIATIONIT.COMPANYCODE = COMPANY.CODE` |
| `FINASSETMASTER_FINASSET` | `COMPANYCODE`, `FINASSETCOUNTERCODE`, `FINASSETCODE` | [`FINASSETMASTER`](../FINANCE/FINASSETMASTER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `FINASSETDEPRECIATIONIT.COMPANYCODE = FINASSETMASTER.COMPANYCODE AND FINASSETDEPRECIATIONIT.FINASSETCOUNTERCODE = FINASSETMASTER.COUNTERCODE AND FINASSETDEPRECIATIONIT.FINASSETCODE = FINASSETMASTER.CODE` |
| `FINBUSINESSUNIT_FINBUSINESSUNIT` | `COMPANYCODE`, `FINBUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINASSETDEPRECIATIONIT.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINASSETDEPRECIATIONIT.FINBUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `FINMAINASSET_FINMAINASSET` | `COMPANYCODE`, `FINMAINASSETBUSINESSUNITCODE`, `FINMAINASSETASSETUGENGRPTECOD`, `FINMAINASSETASSETCODE`, `FINMAINASSETCODE` | [`FINMAINASSET`](../FINANCE/FINMAINASSET.md) | `COMPANYCODE`, `BUSINESSUNITCODE`, `ASSETUSERGENERICGROUPTYPECODE`, `ASSETCODE`, `CODE` | RESTRICT | `FINASSETDEPRECIATIONIT.COMPANYCODE = FINMAINASSET.COMPANYCODE AND FINASSETDEPRECIATIONIT.FINMAINASSETBUSINESSUNITCODE = FINMAINASSET.BUSINESSUNITCODE AND FINASSETDEPRECIATIONIT.FINMAINASSETASSETUGENGRPTECOD = FINMAINASSET.ASSETUSERGENERICGROUPTYPECODE AND FINASSETDEPRECIATIONIT.FINMAINASSETASSETCODE = FINMAINASSET.ASSETCODE AND FINASSETDEPRECIATIONIT.FINMAINASSETCODE = FINMAINASSET.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINASSETDEPRECIATIONITUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINBUSINESSUNITCODE,
       t.FINASSETCOUNTERCODE,
       t.FINASSETCODE,
       t.FINYEARTODATE,
       t.ADDITIONALFLAG,
       t.FINMAINASSETBUSINESSUNITCODE,
       t.FINMAINASSETASSETUGENGRPTECOD,
       t.FINMAINASSETASSETCODE,
       t.FINMAINASSETCODE,
       t.DEPRECIATIONAMOUNT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.FINASSETDEPRECIATIONIT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
