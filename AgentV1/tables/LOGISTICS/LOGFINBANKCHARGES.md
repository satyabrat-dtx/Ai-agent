# DB2ADMIN.LOGFINBANKCHARGES

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 80
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 226759

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TYPE` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `BANKCODECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `BANKCODECODE` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 5 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 6 | `LOCCCINTEREST` | DECIMAL(8,2) |  |  |  |  |
| 7 | `LOCBANKSACCHRGE` | DECIMAL(8,2) |  |  |  |  |
| 8 | `LOCPERTHOUSAND` | DECIMAL(8,2) |  |  |  |  |
| 9 | `LOCBANKCHARGE` | DECIMAL(8,2) |  |  |  |  |
| 10 | `IMPLCCOMMSIGHTPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 11 | `IMPOTHERCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 12 | `IMPFORWARDCONTRACTBOOKING` | DECIMAL(18,5) |  |  |  |  |
| 13 | `IMPLCCOMADDSIGHTPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 14 | `IMPFORWARDCONTRACTCANCELLATION` | DECIMAL(18,5) |  |  |  |  |
| 15 | `IMPPERIOD` | CHAR(1) |  |  |  |  |
| 16 | `IMPADDPERIOD` | CHAR(3) |  |  |  |  |
| 17 | `IMPUSANCE` | DECIMAL(8,2) |  |  |  |  |
| 18 | `IMPADDPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 19 | `IMPPERIOD1` | CHAR(1) |  |  |  |  |
| 20 | `IMPADDPERIOD1` | CHAR(3) |  |  |  |  |
| 21 | `IMPLCTELEX` | DECIMAL(8,2) |  |  |  |  |
| 22 | `IMPLCCLEARINGCOMMISION` | DECIMAL(8,2) |  |  |  |  |
| 23 | `IMPLCCLEARINGCHARGES` | DECIMAL(8,2) |  |  |  |  |
| 24 | `IMPLCAMENDMENT` | DECIMAL(8,2) |  |  |  |  |
| 25 | `IMPNONLCPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 26 | `IMPNONLCOTHERCHARGES` | DECIMAL(8,2) |  |  |  |  |
| 27 | `IMPADVANCEPAYMENT` | DECIMAL(18,5) |  |  |  |  |
| 28 | `NEGBANKCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `NEGBANKCODE` | CHAR(20) |  |  |  |  |
| 30 | `NEGLCTELEX` | DECIMAL(8,2) |  |  |  |  |
| 31 | `NEGSIGHTLTDAYS` | DECIMAL(8,2) |  |  |  |  |
| 32 | `NEGSIGHTGTDAYS` | DECIMAL(8,2) |  |  |  |  |
| 33 | `NEGEXPBILLCOMMISSION` | DECIMAL(8,2) |  |  |  |  |
| 34 | `NEGAGENCYDDCOMMISSION` | DECIMAL(8,2) |  |  |  |  |
| 35 | `NEGAGENCYTTCOMMISSION` | DECIMAL(8,2) |  |  |  |  |
| 36 | `NEGAGENCYBANKCHARGES` | DECIMAL(8,2) |  |  |  |  |
| 37 | `NEGWTPCGPREMIUMPERMON` | CHAR(3) |  |  |  |  |
| 38 | `NEGEXPORTADVBANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 39 | `NEGSERVICETAXONBANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 40 | `NEGOTHERCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 41 | `NEGBANKCERTIFICATE` | DECIMAL(8,2) |  |  |  |  |
| 42 | `NEGINTERESTSIGHTWITHSUB` | DECIMAL(5,2) |  |  |  |  |
| 43 | `NEGINTERESTSIGHTWITHOUTSUB` | DECIMAL(5,2) |  |  |  |  |
| 44 | `NEGUSANCESIGHTWITHOUTSUBLT` | CHAR(3) |  |  |  |  |
| 45 | `NEGUSANCESIGHTWITHOUTSUBGT` | CHAR(3) |  |  |  |  |
| 46 | `NEGPOSTAGE` | DECIMAL(8,2) |  |  |  |  |
| 47 | `NEGEXPORTBILL` | CHAR(1) |  |  |  |  |
| 48 | `NEGODINTERESTONEXPORTBILLS` | CHAR(3) |  |  |  |  |
| 49 | `NEGPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 50 | `RELFCCHARGES` | DECIMAL(8,2) |  |  |  |  |
| 51 | `RELINTERESTWITHOUTSUB` | CHAR(3) |  |  |  |  |
| 52 | `RELCANCELLATION` | DECIMAL(8,2) |  |  |  |  |
| 53 | `RELPACKINGBOOKINGCREDITCHARGES` | DECIMAL(8,2) |  |  |  |  |
| 54 | `RELPACKINGCREDITINTEREST` | DECIMAL(8,2) |  |  |  |  |
| 55 | `RELOVERDUEINTEREST` | DECIMAL(8,2) |  |  |  |  |
| 56 | `RELBILLSREALISATIONCHARGES` | DECIMAL(8,2) |  |  |  |  |
| 57 | `COLBANKCODECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `COLBANKCODECODE` | CHAR(20) |  |  |  |  |
| 59 | `COLFROMDATE` | DATE |  |  |  |  |
| 60 | `COLTODATE` | DATE |  |  |  |  |
| 61 | `COLFROMAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 62 | `COLTOAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 63 | `COLRATE` | DECIMAL(18,5) |  |  |  |  |
| 64 | `COLMINAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 65 | `COLMAXAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 66 | `COLOTHERCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 67 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 68 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 69 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 70 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 71 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 72 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 73 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 74 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 75 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 76 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 77 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 78 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 79 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINBANKCHARGES.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TYPE,
       t.BANKCODECOMPANYCODE,
       t.BANKCODECODE,
       t.FROMDATE,
       t.TODATE,
       t.LOCCCINTEREST,
       t.LOCBANKSACCHRGE,
       t.LOCPERTHOUSAND,
       t.LOCBANKCHARGE,
       t.IMPLCCOMMSIGHTPERCENTAGE,
       t.IMPOTHERCHARGES
FROM   DB2ADMIN.LOGFINBANKCHARGES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
