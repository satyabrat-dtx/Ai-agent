# DB2ADMIN.RECRUITMISCELLANEOUS

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`, `SERIALNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159900

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SERIALNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `LOCATIONPREF` | CHAR(100) | NOT NULL |  |  |  |
| 4 | `INTERVIEWBYTHISGRP` | INTEGER | NOT NULL |  |  |  |
| 5 | `RMCOMPANYNAME` | CHAR(100) |  |  |  |  |
| 6 | `PREVIOUSPOSITION` | CHAR(100) |  |  |  |  |
| 7 | `OFFER` | INTEGER | NOT NULL |  |  |  |
| 8 | `RFNJOINING` | CHAR(100) |  |  |  |  |
| 9 | `PREVIOUSEMPLOYED` | INTEGER | NOT NULL |  |  |  |
| 10 | `RFLEAVING` | CHAR(100) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITMISCELLANEOUS.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITMISCELLANEOUS.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITMISCELLANEOUS.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITMISCELLANEOUSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.SERIALNUMBER,
       t.LOCATIONPREF,
       t.INTERVIEWBYTHISGRP,
       t.RMCOMPANYNAME,
       t.PREVIOUSPOSITION,
       t.OFFER,
       t.RFNJOINING,
       t.PREVIOUSEMPLOYED,
       t.RFLEAVING,
       t.CREATIONDATETIME
FROM   DB2ADMIN.RECRUITMISCELLANEOUS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
