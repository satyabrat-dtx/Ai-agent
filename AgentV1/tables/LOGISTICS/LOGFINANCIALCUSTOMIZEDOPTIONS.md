# DB2ADMIN.LOGFINANCIALCUSTOMIZEDOPTIONS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 61
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 102278

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTRYDOMESTICCODE` | CHAR(3) |  |  |  |  |
| 2 | `FINANCIALDIVISIONUSED` | SMALLINT | NOT NULL |  |  |  |
| 3 | `JOURNALACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `JOURNALCODE` | CHAR(10) |  |  |  |  |
| 5 | `JOURNALFREQUENCYTYPE` | CHAR(1) |  |  |  |  |
| 6 | `TOLERANCEAMOUNTDEBITCREDIT` | DECIMAL(7,2) | NOT NULL |  |  |  |
| 7 | `CHECKGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 8 | `CHECKMINMAXGLACCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 9 | `MINLENGTHGLACCOUNT` | INTEGER | NOT NULL |  |  |  |
| 10 | `MAXLENGTHGLACCOUNT` | INTEGER | NOT NULL |  |  |  |
| 11 | `SYNTHETICACCOUNTS` | SMALLINT | NOT NULL |  |  |  |
| 12 | `MAXLENGTHSYNTHETIC` | INTEGER | NOT NULL |  |  |  |
| 13 | `CHECKPREVLEVEL` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CROSSCHECKACCOUNTDEF` | SMALLINT | NOT NULL |  |  |  |
| 15 | `DEFAULTREMINDERLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 16 | `DEFAULTREMINDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 17 | `HIGHESTREMINDERLEVEL` | INTEGER | NOT NULL |  |  |  |
| 18 | `REMINDERFREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 19 | `TOLERANCEDAYSDOMESTIC` | INTEGER | NOT NULL |  |  |  |
| 20 | `TOLERANCEDAYSFOREIGN` | INTEGER | NOT NULL |  |  |  |
| 21 | `CLEARINGDURINGREMINDER` | SMALLINT | NOT NULL |  |  |  |
| 22 | `DUEDATEFORNETPAYMENT` | CHAR(1) | NOT NULL |  |  |  |
| 23 | `ANTICIPATIONDAYS` | INTEGER | NOT NULL |  |  |  |
| 24 | `RECOURSEDAYS` | INTEGER | NOT NULL |  |  |  |
| 25 | `SUMMARIZECASHINTRANSIT` | SMALLINT | NOT NULL |  |  |  |
| 26 | `CREDITORIDENTIFIER` | CHAR(35) |  |  |  |  |
| 27 | `PAYMENTPROPOSALCNTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `PAYMENTPROPOSALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 29 | `RMDPROPOSALCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `REMINDERPROPOSALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 31 | `GENERALLDGRFIRSTUSERGRPCMYCOD` | CHAR(3) |  |  |  |  |
| 32 | `GENERALLDGRFIRSTUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 33 | `GENERALLDGRSNDUSERGRPCMYCODE` | CHAR(3) |  |  |  |  |
| 34 | `GENERALLDGRSNDUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 35 | `GENERALLDGRTHIRDUSERGRPCMYCOD` | CHAR(3) |  |  |  |  |
| 36 | `GENERALLDGRTHIRDUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 37 | `GENERALLDGRFOURTHUSERGRPCMYCOD` | CHAR(3) |  |  |  |  |
| 38 | `GENERALLDGRFOURTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 39 | `GENERALLDGRFIFTHUSERGRPCMYCOD` | CHAR(3) |  |  |  |  |
| 40 | `GENERALLDGRFIFTHUSERGROUPCODE` | CHAR(3) |  |  |  |  |
| 41 | `BALFIRSTREPORTCODE` | CHAR(3) |  |  |  |  |
| 42 | `BALSECONDREPORTCODE` | CHAR(3) |  |  |  |  |
| 43 | `PLOFIRSTREPORTCODE` | CHAR(3) |  |  |  |  |
| 44 | `PLOSECONDREPORTCODE` | CHAR(3) |  |  |  |  |
| 45 | `BABFIRSTREPORTCODE` | CHAR(3) |  |  |  |  |
| 46 | `BABSECONDREPORTCODE` | CHAR(3) |  |  |  |  |
| 47 | `BWAFIRSTREPORTCODE` | CHAR(3) |  |  |  |  |
| 48 | `BWASECONDREPORTCODE` | CHAR(3) |  |  |  |  |
| 49 | `OTHFIRSTREPORTCODE` | CHAR(3) |  |  |  |  |
| 50 | `OTHSECONDREPORTCODE` | CHAR(3) |  |  |  |  |
| 51 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 52 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 53 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 54 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 55 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 56 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 57 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 58 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 59 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 60 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINANCIALCUSTOMIZEDOPTIONS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTRYDOMESTICCODE,
       t.FINANCIALDIVISIONUSED,
       t.JOURNALACTIVE,
       t.JOURNALCODE,
       t.JOURNALFREQUENCYTYPE,
       t.TOLERANCEAMOUNTDEBITCREDIT,
       t.CHECKGLACCOUNTCODE,
       t.CHECKMINMAXGLACCOUNT,
       t.MINLENGTHGLACCOUNT,
       t.MAXLENGTHGLACCOUNT,
       t.SYNTHETICACCOUNTS
FROM   DB2ADMIN.LOGFINANCIALCUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
