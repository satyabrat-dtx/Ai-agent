# DB2ADMIN.PLANLIST

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `GROUPNUMBER`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42557

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `GROUPNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `EXPLOSIONFAMILYCODE` | BIGINT | NOT NULL |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `STARTPROCESS` | TIMESTAMP |  |  |  |  |
| 5 | `ENDPROCESS` | TIMESTAMP |  |  |  |  |
| 6 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 7 | `ERRORMSG` | CHAR(140) |  |  |  |  |
| 8 | `MINIMUMSTARTDATETIME` | TIMESTAMP |  |  |  |  |
| 9 | `ORIGINENTITY` | INTEGER | NOT NULL |  |  |  |
| 10 | `HIGHPRIORITY` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PLANLIST.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PLANLIST_PLANLISTLINE` | [`PLANLISTLINE`](../OTHER/PLANLISTLINE.md) | `PLANLISTCOMPANYCODE`, `PLANLISTGROUPNUMBER` | `PLANLISTLINE.PLANLISTCOMPANYCODE = PLANLIST.COMPANYCODE AND PLANLISTLINE.PLANLISTGROUPNUMBER = PLANLIST.GROUPNUMBER` |
| `PLANLIST_PLANLISTDETAILS` | [`PLANLISTDETAILS`](../OTHER/PLANLISTDETAILS.md) | `PLANLISTCOMPANYCODE`, `PLANLISTGROUPNUMBER` | `PLANLISTDETAILS.PLANLISTCOMPANYCODE = PLANLIST.COMPANYCODE AND PLANLISTDETAILS.PLANLISTGROUPNUMBER = PLANLIST.GROUPNUMBER` |

## Indexes

- `FAMILYCODE` (EXPLOSIONFAMILYCODE)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.GROUPNUMBER,
       t.EXPLOSIONFAMILYCODE,
       t.DIVISIONCODE,
       t.STARTPROCESS,
       t.ENDPROCESS,
       t.STATUS,
       t.ERRORMSG,
       t.MINIMUMSTARTDATETIME,
       t.ORIGINENTITY,
       t.HIGHPRIORITY,
       t.CREATIONDATETIME
FROM   DB2ADMIN.PLANLIST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
