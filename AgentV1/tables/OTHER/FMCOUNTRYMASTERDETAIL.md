# DB2ADMIN.FMCOUNTRYMASTERDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `SCHEMETYPECODE`, `COUNTRYCODE`, `EFFECTIVEDATEFROM`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121830

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SCHEMETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COUNTRYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EFFECTIVEDATEFROM` | DATE | NOT NULL | PK | primary_key |  |
| 4 | `EFFECTIVEDATETO` | DATE |  |  |  |  |
| 5 | `RATE` | DECIMAL(5,2) |  |  |  |  |
| 6 | `REMARKS` | VARCHAR(1000) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FMCOUNTRYMASTERDETAIL.COMPANYCODE = COMPANY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `FMCOUNTRYMASTERDETAIL.COUNTRYCODE = COUNTRY.CODE` |
| `SCHEMETYPE_SCHEMETYPE` | `COMPANYCODE`, `SCHEMETYPECODE` | [`SCHEMETYPE`](../OTHER/SCHEMETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FMCOUNTRYMASTERDETAIL.COMPANYCODE = SCHEMETYPE.COMPANYCODE AND FMCOUNTRYMASTERDETAIL.SCHEMETYPECODE = SCHEMETYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FMCOUNTRYMASTERDETAIL_DETAIL` | [`FMCOUNTRYMASTERDETAILLINE`](../OTHER/FMCOUNTRYMASTERDETAILLINE.md) | `FMCNYMASTERDETAILCOMPANYCODE`, `FMCNYMDETAILSCHEMETYPECODE`, `FMCNYMASTERDETAILCOUNTRYCODE`, `FMCNYMDETAILEFFECTIVEDATEFROM` | `FMCOUNTRYMASTERDETAILLINE.FMCNYMASTERDETAILCOMPANYCODE = FMCOUNTRYMASTERDETAIL.COMPANYCODE AND FMCOUNTRYMASTERDETAILLINE.FMCNYMDETAILSCHEMETYPECODE = FMCOUNTRYMASTERDETAIL.SCHEMETYPECODE AND FMCOUNTRYMASTERDETAILLINE.FMCNYMASTERDETAILCOUNTRYCODE = FMCOUNTRYMASTERDETAIL.COUNTRYCODE AND FMCOUNTRYMASTERDETAILLINE.FMCNYMDETAILEFFECTIVEDATEFROM = FMCOUNTRYMASTERDETAIL.EFFECTIVEDATEFROM` |

## Indexes

- `FMCOUNTRYMASTERDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SCHEMETYPECODE,
       t.COUNTRYCODE,
       t.EFFECTIVEDATEFROM,
       t.EFFECTIVEDATETO,
       t.RATE,
       t.REMARKS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FMCOUNTRYMASTERDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
