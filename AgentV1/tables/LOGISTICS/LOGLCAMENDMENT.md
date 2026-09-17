# DB2ADMIN.LOGLCAMENDMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 76
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 220835

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LCDETAILLCNO` | CHAR(35) | NOT NULL |  |  |  |
| 2 | `LCDETAILLCDATE` | DATE | NOT NULL |  |  |  |
| 3 | `LCAMENDMENTNO` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `LCAMENDMENTDATE` | DATE | NOT NULL |  |  |  |
| 5 | `LCAMENDMENTCHARGES` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 6 | `LCAMENDMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 7 | `LCAMENDMENTEXCHANGERATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `LCRECEIVEDDATE` | DATE | NOT NULL |  |  |  |
| 9 | `LCEXPIRYDATE` | DATE | NOT NULL |  |  |  |
| 10 | `LCEXTENSIONDATE` | DATE |  |  |  |  |
| 11 | `LCTRANSFERFLAG` | INTEGER | NOT NULL |  |  |  |
| 12 | `LCTYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `LCOPENINGPARTYTYPE` | CHAR(1) |  |  |  |  |
| 14 | `LCOPENINGPARTYCODE` | CHAR(8) |  |  |  |  |
| 15 | `LCOPENINGBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 16 | `LCOPENINGBANKCODE` | CHAR(15) |  |  |  |  |
| 17 | `LCOPENINGBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 18 | `LCADVISORYBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 19 | `LCADVISORYBANKCODE` | CHAR(15) |  |  |  |  |
| 20 | `LCADVISORYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 21 | `LCBENEFICIARYCODECODE` | CHAR(3) |  |  |  |  |
| 22 | `LCBENEFICIARYBANKBANKCNYCODE` | CHAR(3) |  |  |  |  |
| 23 | `LCBENEFICIARYBANKCODE` | CHAR(15) |  |  |  |  |
| 24 | `LCBENEFICIARYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 25 | `LCTERMSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `LCTERMSCODE` | CHAR(3) |  |  |  |  |
| 27 | `LCCONTRACTTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `LCCONTRACTTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `ORDERPRESENT` | INTEGER | NOT NULL |  |  |  |
| 30 | `ARTICLEDESCRIPTION1` | VARCHAR(200) |  |  |  |  |
| 31 | `ARTICLEDESCRIPTION2` | VARCHAR(200) |  |  |  |  |
| 32 | `ARTICLEDESCRIPTION3` | VARCHAR(200) |  |  |  |  |
| 33 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 34 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 35 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 36 | `LCAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 37 | `FOREIGNCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 38 | `LCAMOUNTFOREIGNCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 39 | `AGENTSCOMMISION` | DECIMAL(5,2) |  |  |  |  |
| 40 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 41 | `LCREMARK1` | VARCHAR(200) |  |  |  |  |
| 42 | `REMARK2` | VARCHAR(200) |  |  |  |  |
| 43 | `REMARK3` | VARCHAR(200) |  |  |  |  |
| 44 | `REMARK4` | VARCHAR(200) |  |  |  |  |
| 45 | `AMENDMENTREMARK1` | VARCHAR(200) | NOT NULL |  |  |  |
| 46 | `AMENDMENTREMARK2` | VARCHAR(200) | NOT NULL |  |  |  |
| 47 | `LCUTILIZATIONFLAG` | INTEGER | NOT NULL |  |  |  |
| 48 | `LCCLOSEFLAG` | INTEGER | NOT NULL |  |  |  |
| 49 | `LCEXPIRYPLACE` | CHAR(35) | NOT NULL |  |  |  |
| 50 | `LCNOMINATION` | CHAR(35) |  |  |  |  |
| 51 | `LCINSPECTION` | CHAR(35) | NOT NULL |  |  |  |
| 52 | `LCTOLERANCE` | DECIMAL(5,2) |  |  |  |  |
| 53 | `LEGALISATIONREQUIRED` | INTEGER | NOT NULL |  |  |  |
| 54 | `LCDESTINATION` | CHAR(35) |  |  |  |  |
| 55 | `PARTIALSHIPMENTFLAG` | INTEGER | NOT NULL |  |  |  |
| 56 | `TRANSHIPMENTALLOWEDFLAG` | INTEGER | NOT NULL |  |  |  |
| 57 | `LCRESTRICTEDWITH` | CHAR(35) |  |  |  |  |
| 58 | `LCADIVISINGCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 59 | `LASTDATEOFSHIPMENT` | DATE |  |  |  |  |
| 60 | `LCCONFIRMINGBANKBANKCNYCODE` | CHAR(3) |  |  |  |  |
| 61 | `LCCONFIRMINGBANKCODE` | CHAR(15) |  |  |  |  |
| 62 | `LCCONFIRMINGBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 63 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 64 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 65 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 66 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 67 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 68 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 69 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 70 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 71 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 72 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 73 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 74 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 75 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGLCAMENDMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGLCAMENDMENTREGISTRY`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LCDETAILLCNO,
       t.LCDETAILLCDATE,
       t.LCAMENDMENTNO,
       t.LCAMENDMENTDATE,
       t.LCAMENDMENTCHARGES,
       t.LCAMENDMENTCURRENCYCODE,
       t.LCAMENDMENTEXCHANGERATE,
       t.LCRECEIVEDDATE,
       t.LCEXPIRYDATE,
       t.LCEXTENSIONDATE,
       t.LCTRANSFERFLAG
FROM   DB2ADMIN.LOGLCAMENDMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
