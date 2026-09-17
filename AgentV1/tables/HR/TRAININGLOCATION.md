# DB2ADMIN.TRAININGLOCATION

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `TRAININGHALLCODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 161509

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRAININGHALLCODE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 2 | `EXTERANALCONTACTPERSON` | VARCHAR(200) | NOT NULL |  |  |  |
| 3 | `FACILITIESAVAILABLE` | CHAR(100) |  |  |  |  |
| 4 | `ADDRESS` | VARCHAR(200) |  |  |  |  |
| 5 | `CITY` | VARCHAR(200) |  |  |  |  |
| 6 | `STATE` | VARCHAR(200) |  |  |  |  |
| 7 | `COUNTRY` | VARCHAR(200) |  |  |  |  |
| 8 | `PRIMARYPHONENO` | CHAR(12) | NOT NULL |  |  |  |
| 9 | `MOBILENO` | CHAR(12) |  |  |  |  |
| 10 | `FAXNUMBER` | CHAR(12) |  |  |  |  |
| 11 | `EMAILID` | CHAR(25) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRAININGLOCATION.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TRAININGLOCATION_TRAININGHALL` | [`TRAININGSCHEDULELOCATION`](../HR/TRAININGSCHEDULELOCATION.md) | `TSDETAILTSCHEDULECOMPANYCODE`, `TRAININGHALLTRAININGHALLCODE` | `TRAININGSCHEDULELOCATION.TSDETAILTSCHEDULECOMPANYCODE = TRAININGLOCATION.COMPANYCODE AND TRAININGSCHEDULELOCATION.TRAININGHALLTRAININGHALLCODE = TRAININGLOCATION.TRAININGHALLCODE` |

## Indexes

- `TRAININGLOCATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRAININGHALLCODE,
       t.EXTERANALCONTACTPERSON,
       t.FACILITIESAVAILABLE,
       t.ADDRESS,
       t.CITY,
       t.STATE,
       t.COUNTRY,
       t.PRIMARYPHONENO,
       t.MOBILENO,
       t.FAXNUMBER,
       t.EMAILID
FROM   DB2ADMIN.TRAININGLOCATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
