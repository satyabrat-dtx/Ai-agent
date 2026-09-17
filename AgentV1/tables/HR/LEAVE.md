# DB2ADMIN.LEAVE

- **Module**: `HR` (high confidence — table name starts with 'LEAVE')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 12 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 153730

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `LEAVEPAYMENTTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `PAIDLEAVEPAYMPERCNT` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 7 | `AUTORUN` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LEAVE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 12

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LEAVE_LEAVE` | [`LEAVEAVAILMENTRULE`](../HR/LEAVEAVAILMENTRULE.md) | `COMPANYCODE`, `LEAVECODE` | `LEAVEAVAILMENTRULE.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEAVAILMENTRULE.LEAVECODE = LEAVE.CODE` |
| `LEAVE_CFLEAVE` | [`LEAVEECFRULE`](../HR/LEAVEECFRULE.md) | `COMPANYCODE`, `CFLEAVECODE` | `LEAVEECFRULE.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEECFRULE.CFLEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`LEAVEECFRULE`](../HR/LEAVEECFRULE.md) | `COMPANYCODE`, `LEAVECODE` | `LEAVEECFRULE.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEECFRULE.LEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`LEAVEENTITLEMENTRULE`](../HR/LEAVEENTITLEMENTRULE.md) | `COMPANYCODE`, `LEAVECODE` | `LEAVEENTITLEMENTRULE.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEENTITLEMENTRULE.LEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`PELEAVECODEMAPPING`](../HR/PELEAVECODEMAPPING.md) | `ATTENDANCEBONUSRULECOMPANYCODE`, `LEAVECODE` | `PELEAVECODEMAPPING.ATTENDANCEBONUSRULECOMPANYCODE = LEAVE.COMPANYCODE AND PELEAVECODEMAPPING.LEAVECODE = LEAVE.CODE` |
| `LEAVE_TYPEOFLEAVE` | [`REIMBCLAIMRULEDETAIL`](../HR/REIMBCLAIMRULEDETAIL.md) | `RECLAIMRULECOMPANYCODE`, `TYPEOFLEAVECODE` | `REIMBCLAIMRULEDETAIL.RECLAIMRULECOMPANYCODE = LEAVE.COMPANYCODE AND REIMBCLAIMRULEDETAIL.TYPEOFLEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`ATTENDANCECORRECTION`](../HR/ATTENDANCECORRECTION.md) | `COMPANYCODE`, `LEAVECODE` | `ATTENDANCECORRECTION.COMPANYCODE = LEAVE.COMPANYCODE AND ATTENDANCECORRECTION.LEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`LEAVEBALANCE`](../HR/LEAVEBALANCE.md) | `COMPANYCODE`, `LEAVECODE` | `LEAVEBALANCE.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEBALANCE.LEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`LEAVEENCASHMENT`](../HR/LEAVEENCASHMENT.md) | `COMPANYCODE`, `LEAVECODE` | `LEAVEENCASHMENT.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEENCASHMENT.LEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`LEAVECANCELLATION`](../HR/LEAVECANCELLATION.md) | `COMPANYCODE`, `LEAVECODE` | `LEAVECANCELLATION.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVECANCELLATION.LEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`LEAVEENTRYINHRS`](../HR/LEAVEENTRYINHRS.md) | `COMPANYCODE`, `LEAVECODE` | `LEAVEENTRYINHRS.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEENTRYINHRS.LEAVECODE = LEAVE.CODE` |
| `LEAVE_LEAVE` | [`LEAVETRANSACTION`](../HR/LEAVETRANSACTION.md) | `COMPANYCODE`, `LEAVECODE` | `LEAVETRANSACTION.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVETRANSACTION.LEAVECODE = LEAVE.CODE` |

## Indexes

- `LEAVEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.LEAVEPAYMENTTYPE,
       t.PAIDLEAVEPAYMPERCNT,
       t.AUTORUN,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.LEAVE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
