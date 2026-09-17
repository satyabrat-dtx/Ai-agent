# DB2ADMIN.REIMBURSEMENTCALENDAR

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `REIMBURSEMENTCODE`, `FROMDATE`, `TODATE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 160568

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `REIMBURSEMENTCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 2 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 3 | `TODATE` | DATE | NOT NULL | PK | primary_key | End of a validity period. |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REIMBURSEMENTCALENDAR.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `REIMBURSEMENTCALENDAR_REIMBURSEMENTCODE` | [`REIMBURSEMENTGRPBALANCE`](../HR/REIMBURSEMENTGRPBALANCE.md) | `COMPANYCODE`, `RECODEREIMBURSEMENTCODE`, `REIMBURSEMENTCODEFROMDATE`, `REIMBURSEMENTCODETODATE` | `REIMBURSEMENTGRPBALANCE.COMPANYCODE = REIMBURSEMENTCALENDAR.COMPANYCODE AND REIMBURSEMENTGRPBALANCE.RECODEREIMBURSEMENTCODE = REIMBURSEMENTCALENDAR.REIMBURSEMENTCODE AND REIMBURSEMENTGRPBALANCE.REIMBURSEMENTCODEFROMDATE = REIMBURSEMENTCALENDAR.FROMDATE AND REIMBURSEMENTGRPBALANCE.REIMBURSEMENTCODETODATE = REIMBURSEMENTCALENDAR.TODATE` |

## Indexes

- `REIMBURSEMENTCALENDARUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.REIMBURSEMENTCODE,
       t.FROMDATE,
       t.TODATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.REIMBURSEMENTCALENDAR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
