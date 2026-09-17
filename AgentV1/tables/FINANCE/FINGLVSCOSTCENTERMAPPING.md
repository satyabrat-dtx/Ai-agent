# DB2ADMIN.FINGLVSCOSTCENTERMAPPING

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `TEMPLATECODE`, `GLCODE`, `FROMDATE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225496

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `GLCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 5 | `GLCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 7 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 8 | `GLVSCOSTCENTERVALREFCODE` | CHAR(20) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINGLVSCOSTCENTERMAPPING.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINGLVSCOSTCENTERMAPPING.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINGLVSCOSTCENTERMAPPING.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINGLVSCOSTCENTERMAPPING.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINGLVSCOSTCENTERMAPPING.GLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINGLVSCOSTCENTERMAPPING_LINE` | [`FINGLVSCOSTCENTERMAPPINGLINE`](../FINANCE/FINGLVSCOSTCENTERMAPPINGLINE.md) | `FINGLVSCOSTCENTERMPCMYCODE`, `FINGLVSCOSTCENTERMPBUNITCODE`, `FINGLVSCOSTCENTERMPTMPCODE`, `FINGLVSCOSTCENTERMAPPINGGLCODE`, `FINGLVSCOSTCENTERMPFROMDATE` | `FINGLVSCOSTCENTERMAPPINGLINE.FINGLVSCOSTCENTERMPCMYCODE = FINGLVSCOSTCENTERMAPPING.COMPANYCODE AND FINGLVSCOSTCENTERMAPPINGLINE.FINGLVSCOSTCENTERMPBUNITCODE = FINGLVSCOSTCENTERMAPPING.BUSINESSUNITCODE AND FINGLVSCOSTCENTERMAPPINGLINE.FINGLVSCOSTCENTERMPTMPCODE = FINGLVSCOSTCENTERMAPPING.TEMPLATECODE AND FINGLVSCOSTCENTERMAPPINGLINE.FINGLVSCOSTCENTERMAPPINGGLCODE = FINGLVSCOSTCENTERMAPPING.GLCODE AND FINGLVSCOSTCENTERMAPPINGLINE.FINGLVSCOSTCENTERMPFROMDATE = FINGLVSCOSTCENTERMAPPING.FROMDATE` |

## Indexes

- `FINGLVSCOSTCENTERMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.TEMPLATECOMPANYCODE,
       t.TEMPLATECODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.FROMDATE,
       t.TODATE,
       t.GLVSCOSTCENTERVALREFCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.FINGLVSCOSTCENTERMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
