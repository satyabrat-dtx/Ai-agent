# DB2ADMIN.MEDICALBILLDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `MEDICALBILLHEADERCOMPANYCODE`, `MEDICALBILLHEADERYEAR`, `MEDICALBILLHEADEREMPLOYEENO`, `MEDICALBIHEADERACCIDENTNOCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167601

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MEDICALBILLHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MEDICALBILLHEADERYEAR` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MEDICALBILLHEADEREMPLOYEENO` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `MEDICALBIHEADERACCIDENTNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `MEDICALTYPE` | INTEGER | NOT NULL | FK | foreign_key |  |
| 6 | `DMSTORECODE` | BIGINT | NOT NULL | FK | foreign_key |  |
| 7 | `DMSNAME` | CHAR(30) |  |  |  |  |
| 8 | `BILLNO` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 9 | `BILLDATE` | DATE | NOT NULL |  |  |  |
| 10 | `AMOUNT` | DECIMAL(11,2) |  |  |  |  |
| 11 | `SUMMARY` | CHAR(100) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MEDICALBILLHEADER_DETAILS` | `MEDICALBILLHEADERCOMPANYCODE`, `MEDICALBILLHEADERYEAR`, `MEDICALBILLHEADEREMPLOYEENO`, `MEDICALBIHEADERACCIDENTNOCODE` | [`MEDICALBILLHEADER`](../HR/MEDICALBILLHEADER.md) | `COMPANYCODE`, `YEAR`, `EMPLOYEENO`, `ACCIDENTNOCODE` | RESTRICT | `MEDICALBILLDETAIL.MEDICALBILLHEADERCOMPANYCODE = MEDICALBILLHEADER.COMPANYCODE AND MEDICALBILLDETAIL.MEDICALBILLHEADERYEAR = MEDICALBILLHEADER.YEAR AND MEDICALBILLDETAIL.MEDICALBILLHEADEREMPLOYEENO = MEDICALBILLHEADER.EMPLOYEENO AND MEDICALBILLDETAIL.MEDICALBIHEADERACCIDENTNOCODE = MEDICALBILLHEADER.ACCIDENTNOCODE` |
| `MEDICAL_DMSTORE` | `MEDICALBILLHEADERCOMPANYCODE`, `MEDICALTYPE`, `DMSTORECODE` | [`MEDICAL`](../HR/MEDICAL.md) | `COMPANYCODE`, `MEDICALTYPE`, `CODE` | RESTRICT | `MEDICALBILLDETAIL.MEDICALBILLHEADERCOMPANYCODE = MEDICAL.COMPANYCODE AND MEDICALBILLDETAIL.MEDICALTYPE = MEDICAL.MEDICALTYPE AND MEDICALBILLDETAIL.DMSTORECODE = MEDICAL.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MEDICALBILLDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MEDICALBILLHEADERCOMPANYCODE,
       t.MEDICALBILLHEADERYEAR,
       t.MEDICALBILLHEADEREMPLOYEENO,
       t.MEDICALBIHEADERACCIDENTNOCODE,
       t.CODE,
       t.MEDICALTYPE,
       t.DMSTORECODE,
       t.DMSNAME,
       t.BILLNO,
       t.BILLDATE,
       t.AMOUNT,
       t.SUMMARY
FROM   DB2ADMIN.MEDICALBILLDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
