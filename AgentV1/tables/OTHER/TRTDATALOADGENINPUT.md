# DB2ADMIN.TRTDATALOADGENINPUT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `TRTDATALOADDATE`, `CARDID`, `EMPLOYEEID`, `PAYROLLTYPECODE`, `ATTENDANCETYPECODE`, `SHIFTCODE`, `DAYSESSION`, `NOOFHOURS`, `ATTENDANCECODE`, `TOCCBCODE`, `UPDATESTAFFATTDFLAG`, `DATAINSERTTIME`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170319

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRTDATALOADDATE` | DATE | NOT NULL | PK | primary_key |  |
| 2 | `CARDID` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 3 | `EMPLOYEEID` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 4 | `PAYROLLTYPECODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 5 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `SHIFTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `DAYSESSION` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `NOOFHOURS` | DECIMAL(5,2) | NOT NULL | PK | primary_key |  |
| 9 | `ATTENDANCECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 10 | `TOCCBCODE` | VARCHAR(100) | NOT NULL | PK | primary_key |  |
| 11 | `UPDATESTAFFATTDFLAG` | SMALLINT | NOT NULL | PK | primary_key |  |
| 12 | `DATAINSERTTIME` | BIGINT | NOT NULL | PK | primary_key |  |
| 13 | `OLDNOOFHOURS` | DECIMAL(5,2) |  |  |  |  |
| 14 | `OLDATTENDANCECODE` | CHAR(3) |  |  |  |  |
| 15 | `OLDTOCCBCODE` | VARCHAR(100) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `INTIME` | TIME |  |  |  |  |
| 23 | `OUTTIME` | TIME |  |  |  |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRTDATALOADGENINPUT.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRTDATALOADGENINPUTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRTDATALOADDATE,
       t.CARDID,
       t.EMPLOYEEID,
       t.PAYROLLTYPECODE,
       t.ATTENDANCETYPECODE,
       t.SHIFTCODE,
       t.DAYSESSION,
       t.NOOFHOURS,
       t.ATTENDANCECODE,
       t.TOCCBCODE,
       t.UPDATESTAFFATTDFLAG
FROM   DB2ADMIN.TRTDATALOADGENINPUT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
