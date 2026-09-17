# DB2ADMIN.WRKFLOWEMPMAPPING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 81
- **Primary key**: `ABSUNIQUEID`, `CREATIONTIMESTAMP`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183432

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LEPAYROLLTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `LEFROMPRL` | INTEGER | NOT NULL |  |  |  |
| 4 | `FINANCIALYEARCODE` | CHAR(6) |  |  |  |  |
| 5 | `OLDACCESSCARDNO` | CHAR(50) |  |  |  |  |
| 6 | `LEATTENDANCETYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `REQUESTERIDCODE` | CHAR(9) |  |  |  |  |
| 8 | `REQUESTERDATE` | DATE |  |  |  |  |
| 9 | `APPROVERIDCODE` | CHAR(9) |  |  |  |  |
| 10 | `EMPROLE` | CHAR(3) |  |  |  |  |
| 11 | `INVGROUPCODE` | CHAR(10) |  |  |  |  |
| 12 | `LEPAYELEMENTTYPE` | CHAR(1) |  |  |  |  |
| 13 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 14 | `ATTENDANCECODE` | CHAR(1) |  |  |  |  |
| 15 | `ACCESSCARDSNO` | DECIMAL(11,0) |  |  |  |  |
| 16 | `INVGROUPITEMCODE` | CHAR(10) |  |  |  |  |
| 17 | `LEPAYELEMENTCODE` | CHAR(6) |  |  |  |  |
| 18 | `TRANSACTIONTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 19 | `TRANSACTIONTYPECODE` | CHAR(6) |  |  |  |  |
| 20 | `NUMBEROFHRS` | DECIMAL(5,2) |  |  |  |  |
| 21 | `ADDRESSTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 22 | `ADDRESSTYPECODE` | CHAR(6) |  |  |  |  |
| 23 | `DOCUMENTTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 24 | `DOCUMENTTYPECODE` | CHAR(6) |  |  |  |  |
| 25 | `EDUCATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 26 | `EDUCATIONCODE` | CHAR(6) |  |  |  |  |
| 27 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 28 | `RELATIONTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 29 | `RELATIONTYPECODE` | CHAR(6) |  |  |  |  |
| 30 | `LANGUAGEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 31 | `LANGUAGECODE` | CHAR(6) |  |  |  |  |
| 32 | `RELATIONSHIPRELATIONTYPECODE` | CHAR(6) |  |  |  |  |
| 33 | `NOMINATIONTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 34 | `NOMINATIONTYPECODE` | CHAR(6) |  |  |  |  |
| 35 | `SERIALNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 36 | `SKILLIDICSTABLECODE` | CHAR(4) |  |  |  |  |
| 37 | `SKILLIDCODE` | CHAR(6) |  |  |  |  |
| 38 | `SNO` | DECIMAL(5,0) |  |  |  |  |
| 39 | `SRNO` | DECIMAL(5,0) |  |  |  |  |
| 40 | `LEAVECALENDARCALENDARCODE` | CHAR(3) |  |  |  |  |
| 41 | `LVCATEGORYCODE` | CHAR(30) |  |  |  |  |
| 42 | `LVSUBCATEGORYCODE` | CHAR(30) |  |  |  |  |
| 43 | `LVDIVISIONCODE` | CHAR(30) |  |  |  |  |
| 44 | `LVFACTORYCODE` | CHAR(30) |  |  |  |  |
| 45 | `LVDEPARTMENTCODE` | CHAR(30) |  |  |  |  |
| 46 | `LEAVECODE` | CHAR(3) |  |  |  |  |
| 47 | `LVEMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 48 | `TIMEOFENTRY` | CHAR(50) |  |  |  |  |
| 49 | `PAYROLLTYPE` | CHAR(50) |  |  |  |  |
| 50 | `ATTENDANCE` | CHAR(50) |  |  |  |  |
| 51 | `PROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 52 | `ATTENDANCEDATE` | DATE |  |  |  |  |
| 53 | `SHIFT` | CHAR(50) |  |  |  |  |
| 54 | `DAYSESSION` | INTEGER | NOT NULL |  |  |  |
| 55 | `ATTEMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 56 | `TRVSERIALNO` | BIGINT | NOT NULL |  |  |  |
| 57 | `TRVTRAVELTYPE` | INTEGER | NOT NULL |  |  |  |
| 58 | `TRVEMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 59 | `TRVTOURSERIALNO` | BIGINT | NOT NULL |  |  |  |
| 60 | `LOANTYPE` | INTEGER | NOT NULL |  |  |  |
| 61 | `LOANCODE` | CHAR(50) |  |  |  |  |
| 62 | `LOANEMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 63 | `LOANSERIALNO` | DECIMAL(10,0) |  |  |  |  |
| 64 | `TRAININGEMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 65 | `TRAININGTYPE` | CHAR(50) |  |  |  |  |
| 66 | `TRAINING` | CHAR(50) |  |  |  |  |
| 67 | `SCHEDULE` | DECIMAL(5,0) |  |  |  |  |
| 68 | `SCHEDULENO` | DECIMAL(5,0) |  |  |  |  |
| 69 | `ESSFMGCODE` | CHAR(3) |  |  |  |  |
| 70 | `ESSASSETCODE` | CHAR(3) |  |  |  |  |
| 71 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 72 | `INTIMATIONNO` | BIGINT | NOT NULL |  |  |  |
| 73 | `INTIMATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 74 | `TRVSETTLEMENTNO` | BIGINT | NOT NULL |  |  |  |
| 75 | `TRVSETTLEMENTTOURNO` | BIGINT | NOT NULL |  |  |  |
| 76 | `CLAIMNO` | BIGINT | NOT NULL |  |  |  |
| 77 | `STATUSFLAG` | INTEGER | NOT NULL |  |  |  |
| 78 | `LTFROMDATE` | DATE |  |  |  |  |
| 79 | `LTTODATE` | DATE |  |  |  |  |
| 80 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFLOWEMPMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LEPAYROLLTYPECODE,
       t.LEFROMPRL,
       t.FINANCIALYEARCODE,
       t.OLDACCESSCARDNO,
       t.LEATTENDANCETYPECODE,
       t.REQUESTERIDCODE,
       t.REQUESTERDATE,
       t.APPROVERIDCODE,
       t.EMPROLE,
       t.INVGROUPCODE
FROM   DB2ADMIN.WRKFLOWEMPMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
