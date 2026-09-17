# DB2ADMIN.INSURANCEPOLICYDETAIL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `INSURANCEPOLICYCOMPANYCODE`, `INSURANCEPOLICYDIVISIONCODE`, `INSURANCEPOLICYPOLICYNO`, `INSURANCEPOLICYPOLICYDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129195

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INSURANCEPOLICYCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INSURANCEPOLICYDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INSURANCEPOLICYPOLICYNO` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `INSURANCEPOLICYPOLICYDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PLANTINVOICECODE` | CHAR(15) |  | FK | foreign_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `INSURANCEPOLICY_LINE` | `INSURANCEPOLICYCOMPANYCODE`, `INSURANCEPOLICYDIVISIONCODE`, `INSURANCEPOLICYPOLICYNO`, `INSURANCEPOLICYPOLICYDATE` | [`INSURANCEPOLICY`](../SALES/INSURANCEPOLICY.md) | `COMPANYCODE`, `DIVISIONCODE`, `POLICYNO`, `POLICYDATE` | RESTRICT | `INSURANCEPOLICYDETAIL.INSURANCEPOLICYCOMPANYCODE = INSURANCEPOLICY.COMPANYCODE AND INSURANCEPOLICYDETAIL.INSURANCEPOLICYDIVISIONCODE = INSURANCEPOLICY.DIVISIONCODE AND INSURANCEPOLICYDETAIL.INSURANCEPOLICYPOLICYNO = INSURANCEPOLICY.POLICYNO AND INSURANCEPOLICYDETAIL.INSURANCEPOLICYPOLICYDATE = INSURANCEPOLICY.POLICYDATE` |
| `PLANTINVOICE_PLANTINVOICE` | `INSURANCEPOLICYCOMPANYCODE`, `INSURANCEPOLICYDIVISIONCODE`, `PLANTINVOICECODE` | [`PLANTINVOICE`](../CORE_MASTER/PLANTINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `INSURANCEPOLICYDETAIL.INSURANCEPOLICYCOMPANYCODE = PLANTINVOICE.COMPANYCODE AND INSURANCEPOLICYDETAIL.INSURANCEPOLICYDIVISIONCODE = PLANTINVOICE.DIVISIONCODE AND INSURANCEPOLICYDETAIL.PLANTINVOICECODE = PLANTINVOICE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INSURANCEPOLICYDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INSURANCEPOLICYCOMPANYCODE,
       t.INSURANCEPOLICYDIVISIONCODE,
       t.INSURANCEPOLICYPOLICYNO,
       t.INSURANCEPOLICYPOLICYDATE,
       t.PLANTINVOICECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.INSURANCEPOLICYDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
