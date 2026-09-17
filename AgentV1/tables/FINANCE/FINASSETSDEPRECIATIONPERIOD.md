# DB2ADMIN.FINASSETSDEPRECIATIONPERIOD

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `DEPPERIODCODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224884

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DEPPERIODCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 2 | `BUSINESUNITGROUPCODE` | CHAR(10) |  | FK | foreign_key |  |
| 3 | `DEPPERIOD` | DATE |  |  |  |  |
| 4 | `ISPOSTED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `POSTEDDATE` | DATE |  |  |  |  |
| 6 | `JOBNUMBER` | BIGINT | NOT NULL |  |  |  |
| 7 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `ASSETFINDOCCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `ASSETFINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 17 | `ASSETFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 18 | `ASSETFINDOCDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 19 | `ASSETFINDOCSTCGROUPCODE` | CHAR(6) |  |  |  |  |
| 20 | `ASSETFINDOCCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINASSETSDEPRECIATIONPERIOD.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESUNITGROUP` | `COMPANYCODE`, `BUSINESUNITGROUPCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINASSETSDEPRECIATIONPERIOD.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINASSETSDEPRECIATIONPERIOD.BUSINESUNITGROUPCODE = FINBUSINESSUNIT.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINASSETSDEPRECIATIONPERIOD_DETAIL` | [`FINASSDEPPERIODDETAIL`](../FINANCE/FINASSDEPPERIODDETAIL.md) | `FINASSDEPPERIODCOMPANYCODE`, `FINASSDEPPERIODDEPPERIODCODE` | `FINASSDEPPERIODDETAIL.FINASSDEPPERIODCOMPANYCODE = FINASSETSDEPRECIATIONPERIOD.COMPANYCODE AND FINASSDEPPERIODDETAIL.FINASSDEPPERIODDEPPERIODCODE = FINASSETSDEPRECIATIONPERIOD.DEPPERIODCODE` |

## Indexes

- `FINASSDEPRECIATIONPERIODUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DEPPERIODCODE,
       t.BUSINESUNITGROUPCODE,
       t.DEPPERIOD,
       t.ISPOSTED,
       t.POSTEDDATE,
       t.JOBNUMBER,
       t.STATUS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FINASSETSDEPRECIATIONPERIOD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
